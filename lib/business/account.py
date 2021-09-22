from lib.business.authorizer import Authorizer
from lib.constants import violations
from lib.repository.statement import statement


# AccountAuthorizer handles all operations related to accounting
# (e.g: account initialization and account violations)
class AccountAuthorizer(Authorizer):

    def review_operation(self, operation):
        if self.should_apply_account_already_initialized_violation():
            self.apply_violation(violations.ACCOUNT_ALREADY_INITIALIZED)
        else:
            statement.create_account(operation["account"])

        statement.set_operation({"operation": operation, "result": self.result})
        self.result["account"] = statement.get_account()
        return self.result

    def should_apply_account_already_initialized_violation(self):
        return statement.is_account_created()
