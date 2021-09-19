import unittest
from unittest.mock import patch

from lib.business.transaction import TransactionAuthorizer


class TestTransactionAuthorizer(unittest.TestCase):

    @patch('lib.repository.statement.Statement.set_account_limit')
    @patch('lib.repository.statement.Statement.get_card_balance')
    @patch('lib.repository.statement.Statement.is_account_created')
    @patch('lib.repository.statement.Statement.get_account')
    def test_review_operation_without_violations(self, mock_statement_get_account,
                                                 mock_statement_is_account_created,
                                                 mock_statement_get_card_balance,
                                                 mock_statement_set_account_limit):
        mock_statement_set_account_limit.return_value = None
        mock_statement_get_card_balance.return_value = 225
        mock_statement_is_account_created.return_value = True
        mock_statement_get_account.return_value = {"active-card": True, "available-limit": 225}

        operation = {"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}}
        result = TransactionAuthorizer().review_operation(operation)
        expected = {"account": {"active-card": True, "available-limit": 225}, "violations": []}
        self.assertEqual(expected, result)

    @patch('lib.repository.statement.Statement.set_account_limit')
    @patch('lib.repository.statement.Statement.get_card_balance')
    @patch('lib.repository.statement.Statement.is_account_created')
    @patch('lib.repository.statement.Statement.get_account')
    def test_review_operation_with_account_not_initialized_violation(self, mock_statement_get_account,
                                                                     mock_statement_is_account_created,
                                                                     mock_statement_get_card_balance,
                                                                     mock_statement_set_account_limit):
        mock_statement_set_account_limit.return_value = None
        mock_statement_get_card_balance.return_value = 225
        mock_statement_is_account_created.return_value = False
        mock_statement_get_account.return_value = {}

        operation = {"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}}
        result = TransactionAuthorizer().review_operation(operation)
        expected = {"account": {}, "violations": ["account-not-initialized"]}
        self.assertEqual(expected, result)

    @patch('lib.repository.statement.Statement.set_account_limit')
    @patch('lib.repository.statement.Statement.get_card_balance')
    @patch('lib.repository.statement.Statement.is_account_created')
    @patch('lib.repository.statement.Statement.get_account')
    def test_review_operation_with_apply_card_not_active(self, mock_statement_get_account,
                                                         mock_statement_is_account_created,
                                                         mock_statement_get_card_balance,
                                                         mock_statement_set_account_limit):

        mock_statement_set_account_limit.return_value = None
        mock_statement_get_card_balance.return_value = 200
        mock_statement_is_account_created.return_value = True
        mock_statement_get_account.return_value = {"active-card": False, "available-limit": 225}

        operation = {"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}}
        result = TransactionAuthorizer().review_operation(operation)
        expected = {"account": {"active-card": False, "available-limit": 225}, "violations": ["card-not-active"]}
        self.assertEqual(expected, result)
