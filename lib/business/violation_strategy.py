from abc import ABC, abstractmethod
from lib.repository.statement import statement
from lib.constants import violations, time
from lib.helpers.time import get_datetime_from_operation_time
from datetime import timedelta
import pydash

class ViolationStrategy(ABC):
    @abstractmethod
    def check_violation(self, operation):
        pass

class AccountNotInitializedStrategy(ViolationStrategy):
    def check_violation(self, _):
        if not statement.is_account_created():
            return violations.ACCOUNT_NOT_INITIALIZED
        return None

class CardNotActiveStrategy(ViolationStrategy):
    def check_violation(self, _):
        account = statement.get_account()
        if not account.get("active-card"):
            return violations.CARD_NOT_ACTIVE
        return None

class InsufficientLimitStrategy(ViolationStrategy):
    def check_violation(self, operation):
        if operation["transaction"]["amount"] > statement.get_card_balance():
            return violations.INSUFFICIENT_LIMIT
        return None

class HighFrequencySmallIntervalStrategy(ViolationStrategy):
    def check_violation(self, operation):
        operations = statement.get_transactions_operations()
        if len(operations) < time.HIGH_FREQUENCY_TRANSACTIONS_COUNT_LIMIT:
            return None

        operation_datetime = get_datetime_from_operation_time(operation)
        operations_inside_time_interval = pydash.filter_(
            operations, lambda op: get_datetime_from_operation_time(op) >= (operation_datetime - timedelta(minutes=2))
        )

        if len(operations_inside_time_interval) >= time.HIGH_FREQUENCY_TRANSACTIONS_COUNT_LIMIT:
            return violations.HIGH_FREQUENCY_SMALL_INTERVAL
        return None

class DoubleTransactionStrategy(ViolationStrategy):
    def check_violation(self, operation):
        operations = statement.get_transactions_operations()
        if len(operations) == 0:
            return None

        equivalent_operations = pydash.filter_(operations,
                                               lambda list_op: self._filter_equivalent_operations_in_time_interval(
                                                   operation, list_op, minutes=time.HIGH_FREQUENCY_TIME_INTERVAL)
                                               )
        if equivalent_operations:
            return violations.DOUBLED_TRANSACTION
        return None

    def _filter_equivalent_operations_in_time_interval(self, op1, op2, minutes):
        is_merchant_equals = op1["transaction"]["merchant"] == op2["transaction"]["merchant"]
        is_amount_equals = op1["transaction"]["amount"] == op2["transaction"]["amount"]

        is_time_inside_interval = get_datetime_from_operation_time(op1) > \
                                  get_datetime_from_operation_time(op2) - timedelta(minutes=minutes)

        return is_merchant_equals and is_amount_equals and is_time_inside_interval
