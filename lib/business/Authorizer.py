from lib.state.statement import statement
from lib.constants import violations


class Authorizer:

    def __init__(self):
        self.result = []

    @staticmethod
    def get_specific_operator_by_operation(operation):
        if "account" in operation:
            return AccountAuthorizer()
        elif "transaction" in operation:
            return TransactionAuthorizer()

    def review_operation(self, operation):
        pass

    def get_violations(self, operation):
        pass


class AccountAuthorizer(Authorizer):

    def review_operation(self, operation):
        self.result = {
            "account": None,
            "violations": []
        }

        if self.should_apply_account_already_initialized_violation():
            self.result["violations"].append(violations.ACCOUNT_ALREADY_INITIALIZED)
        else:
            statement.create_account(operation["account"])
            self.result["account"] = statement.account

        return self.result

    def should_apply_account_already_initialized_violation(self):
        return statement.is_account_created()


class TransactionAuthorizer(Authorizer):

    def review_operation(self, operation):
        pass
