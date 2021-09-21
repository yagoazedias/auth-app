import unittest

from lib.repository.statement import statement


class TestStatementInterface(unittest.TestCase):

    # Cleaning state after each test
    def tearDown(self):
        statement._clean_up()

    def test_create_account(self):
        statement.create_account({"active-card": False, "available-limit": 100})
        self.assertIsNotNone(statement.account)

    def test_create_account_fail_on_duplicated_account(self):
        statement.create_account({"active-card": False, "available-limit": 100})

        with self.assertRaises(Exception):
            statement.create_account({"active-card": False, "available-limit": 100})

    def test_get_account_for_not_created_account(self):
        statement.account = {"active-card": False, "available-limit": 100}
        self.assertEqual(statement.get_account(), {"active-card": False, "available-limit": 100})

    def test_is_account_created(self):
        self.assertFalse(statement.is_account_created())
        statement.account = {"active-card": False, "available-limit": 100}
        self.assertTrue(statement.is_account_created())

    def test_set_operation(self):
        statement.set_operation({"operation": "", "result": ""})
        self.assertEqual(len(statement.operations), 1)
        self.assertEqual(statement.operations[0], {"operation": "", "result": ""})

    def test_get_operations(self):
        operations = statement.get_operations()
        self.assertEqual(len(operations), 0)

        statement.set_operation({"operation": "", "result": ""})
        self.assertEqual(operations[0], {"operation": "", "result": ""})

    def test_get_transactions_operations(self):
        transactions = [{"operation": {"transaction": "1"}, "result": {"violations": []}},
                        {"operation": {"transaction": "2"}, "result": {"violations": []}}]

        statement.set_operation({"operation": {"account": "1"}, "result": {"violations": []}})
        statement.set_operation({"operation": {"transaction": "1"}, "result": {"violations": []}})
        statement.set_operation({"operation": {"transaction": "2"}, "result": {"violations": []}})

        results = statement.get_transactions_operations()
        self.assertEqual(len(transactions), len(results))

        for i in range(0, len(results)):
            self.assertEqual(transactions[i]["operation"], results[i])

    def test_get_card_balance(self):
        self.assertEqual(statement.get_card_balance(), 0)
        statement.create_account({"active-card": False, "available-limit": 100})
        self.assertEqual(statement.get_card_balance(), 100)

    def test_set_account_limit(self):
        statement.create_account({"active-card": False, "available-limit": 0})
        self.assertEqual(statement.account["available-limit"], 0)

        statement.set_account_limit(100)
        self.assertEqual(statement.account["available-limit"], 100)
