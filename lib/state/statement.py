# Statement is responsible for generating the statement of the aplication, 
# keeping track of the transactions and the balance.
# Other classes will use this class to update the statement.
class Statement:

    def __init__(self):
        self._operations = []
        self.account = None

    def create_account(self, account):
        if self.is_account_created():
            raise Exception("Account already created")
        self.account = account

    def is_account_created(self):
        return self.account is not None

    def set_operation(self, operation):
        return self._operations.append(operation)


statement = Statement()
