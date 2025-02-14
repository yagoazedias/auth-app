from lib.repository.statement import statement
from lib.constants import violations
from lib.business.authorizer import Authorizer
from lib.business.violation_strategy import (
    AccountNotInitializedStrategy,
    CardNotActiveStrategy,
    InsufficientLimitStrategy,
    HighFrequencySmallIntervalStrategy,
    DoubleTransactionStrategy
)

# TransactionAuthorizer will handle all operations related to transaction
# (e.g: transaction attempt, transaction violations)
class TransactionAuthorizer(Authorizer):
    def __init__(self):
        super().__init__()
        self.strategies = [
            AccountNotInitializedStrategy(),
            CardNotActiveStrategy(),
            InsufficientLimitStrategy(),
            HighFrequencySmallIntervalStrategy(),
            DoubleTransactionStrategy()
        ]

    def review_operation(self, operation):
        for strategy in self.strategies:
            violation = strategy.check_violation(operation)
            if violation:
                self.apply_violation(violation)
            if violation in [violations.ACCOUNT_NOT_INITIALIZED, violations.CARD_NOT_ACTIVE]:
                return self.evaluate_operation(operation)

        return self.evaluate_operation(operation)

    def evaluate_operation(self, operation):
        balance = statement.get_card_balance()
        transaction_amount = operation["transaction"]["amount"]

        if not self.has_violations():
            statement.set_account_limit(balance - transaction_amount)

        self.result["account"] = statement.get_account()

        if not self.has_violations():
            statement.set_operation({"operation": operation, "result": self.result})

        return self.result

    def has_violations(self):
        return len(self.result.get("violations")) != 0
