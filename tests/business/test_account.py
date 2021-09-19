import unittest
from unittest.mock import patch

from lib.business.account import AccountAuthorizer


class TestAccountAuthorizer(unittest.TestCase):

    @patch('lib.business.account.AccountAuthorizer.should_apply_account_already_initialized_violation')
    @patch('lib.repository.statement.Statement.create_account')
    @patch('lib.repository.statement.Statement.get_account')
    def test_review_operation_with_already_initialized_violation(self, mock_statement_get_account,
                                                                 mock_statement_create_account, mock_account):
        account_authorizer = AccountAuthorizer()
        mock_account.return_value = True
        mock_statement_get_account.return_value = {}
        mock_statement_create_account.return_value = None

        operation = {"account": {"active-card": False, "available-limit": 225}}

        result = account_authorizer.review_operation(operation)
        expected = {"account": {}, "violations": ["account-already-initialized"]}

        self.assertEqual(expected, result)

    @patch('lib.business.account.AccountAuthorizer.should_apply_account_already_initialized_violation')
    @patch('lib.repository.statement.Statement.create_account')
    @patch('lib.repository.statement.Statement.get_account')
    def test_review_operation_without_violations(self, mock_statement_get_account,
                                                 mock_statement_create_account, mock_account):
        account_authorizer = AccountAuthorizer()
        account = {"active-card": True, "available-limit": 225}
        mock_account.return_value = False
        mock_statement_create_account.return_value = None
        mock_statement_get_account.return_value = account

        operation = {"account": account}
        result = account_authorizer.review_operation(operation)
        expected = {"account": account, "violations": []}

        self.assertEqual(expected, result)

    @patch('lib.repository.statement.Statement.is_account_created')
    def test_should_apply_account_already_initialized_violation(self, mock):
        account_authorizer = AccountAuthorizer()
        mock.return_value = True
        expected = True

        result = account_authorizer.should_apply_account_already_initialized_violation()
        self.assertEqual(expected, result)
