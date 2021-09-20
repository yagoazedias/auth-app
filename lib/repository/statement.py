import pydash


# Statement is responsible for generating the statement of the application,
# keeping track of the transactions and the balance.
# Other classes will use this class to update the statement.
class Statement:

    def __init__(self):
        self.operations = []
        self.account = {}
        self.original_limit = 0

    def create_account(self, account):
        if self.is_account_created():
            raise Exception("Account already created")
        self.account = account
        self.original_limit = self.account["available-limit"]

    def get_account(self):
        return self.account

    def is_account_created(self):
        return len(self.account) > 0

    def set_operation(self, operation):
        return self.operations.append(operation)

    def get_operations(self):
        return self.operations

    def get_transactions_operations(self):
        operations = pydash.filter_(self.operations, lambda op: "transaction" in op["operation"] and len(op["result"]["violations"]) == 0)
        transactions = pydash.map_(operations, lambda operation: operation["operation"])
        return transactions

    def get_card_balance(self):
        return self.account.get("available-limit", 0)

    def set_account_limit(self, limit):
        self.account = {**self.account, "available-limit": limit}


statement = Statement()
