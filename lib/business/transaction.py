from lib.repository.statement import statement
from lib.constants import violations
from lib.business.authorizer import Authorizer


# TransactionAuthorizer will handle all operations related to transaction
# (e.g: transaction attempt, transaction violations)
class TransactionAuthorizer(Authorizer):

    def review_operation(self, operation):
        if self.should_apply_account_not_initialized_violation():
            self.result["violations"].append(violations.ACCOUNT_NOT_INITIALIZED)
        elif self.should_apply_card_not_active():
            self.result["violations"].append(violations.CARD_NOT_ACTIVE)
        else:
            balance = statement.get_card_balance()
            transaction_amount = operation["transaction"]["amount"]

            if balance > transaction_amount:
                statement.set_account_limit(balance - transaction_amount)

        self.result["account"] = statement.get_account()
        return self.result

    def should_apply_account_not_initialized_violation(self):
        return not statement.is_account_created()

    def should_apply_card_not_active(self):
        account = statement.get_account()
        return not account.get("active-card")
