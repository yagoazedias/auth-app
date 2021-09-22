import pydash

from datetime import timedelta

from lib.repository.statement import statement
from lib.constants import violations, time
from lib.business.authorizer import Authorizer

from lib.helpers.time import get_datetime_from_operation_time


# TransactionAuthorizer will handle all operations related to transaction
# (e.g: transaction attempt, transaction violations)
class TransactionAuthorizer(Authorizer):

    def review_operation(self, operation):
        # Account Not Initialized and Card Not Active violations returns the evaluated_operation immediately,
        # because the following violations requires at least a created account.
        if self.should_apply_account_not_initialized_violation():
            self.apply_violation(violations.ACCOUNT_NOT_INITIALIZED)
            return self.evaluate_operation(operation)

        if self.should_apply_card_not_active():
            self.apply_violation(violations.CARD_NOT_ACTIVE)
            return self.evaluate_operation(operation)

        if self.should_apply_insufficient_limit(operation):
            self.apply_violation(violations.INSUFFICIENT_LIMIT)

        if self.should_apply_high_frequency_small_interval(operation):
            self.apply_violation(violations.HIGH_FREQUENCY_SMALL_INTERVAL)

        if self.should_apply_double_transaction(operation):
            self.apply_violation(violations.DOUBLED_TRANSACTION)

        return self.evaluate_operation(operation)

    def evaluate_operation(self, operation):
        balance = statement.get_card_balance()
        transaction_amount = operation["transaction"]["amount"]

        if not self.has_violations():
            statement.set_account_limit(balance - transaction_amount)

        self.result["account"] = statement.get_account()
        statement.set_operation({"operation": operation, "result": self.result})

        return self.result

    def has_violations(self):
        return len(self.result.get("violations")) != 0

    def should_apply_account_not_initialized_violation(self):
        return not statement.is_account_created()

    def should_apply_card_not_active(self):
        account = statement.get_account()
        return not account.get("active-card")

    def should_apply_insufficient_limit(self, operation):
        return operation["transaction"]["amount"] > statement.get_card_balance()

    # Review this functions because it considers only the last transaction, should consider all previous transactions
    # that does not have a violation
    def should_apply_high_frequency_small_interval(self, operation):
        operations = statement.get_transactions_operations()
        if len(operations) < time.HIGH_FREQUENCY_TRANSACTIONS_COUNT_LIMIT:
            return False

        operation_datetime = get_datetime_from_operation_time(operation)
        operations_inside_time_interval = pydash.filter_(
            operations, lambda op: get_datetime_from_operation_time(op) >= (operation_datetime - timedelta(minutes=2))
        )

        return len(operations_inside_time_interval) >= time.HIGH_FREQUENCY_TRANSACTIONS_COUNT_LIMIT

    def should_apply_double_transaction(self, operation):
        operations = statement.get_transactions_operations()
        if len(operations) == 0:
            return False

        equivalent_operations = pydash.filter_(operations,
                                               lambda list_op: self._filter_equivalent_operations_in_time_interval(
                                                   operation, list_op, minutes=time.HIGH_FREQUENCY_TIME_INTERVAL)
                                               )
        return equivalent_operations

    def _filter_equivalent_operations_in_time_interval(self, op1, op2, minutes):
        is_merchant_equals = op1["transaction"]["merchant"] == op2["transaction"]["merchant"]
        is_amount_equals = op1["transaction"]["amount"] == op2["transaction"]["amount"]

        is_time_inside_interval = get_datetime_from_operation_time(op1) > \
                                  get_datetime_from_operation_time(op2) - timedelta(minutes=minutes)

        return is_merchant_equals and is_amount_equals and is_time_inside_interval
