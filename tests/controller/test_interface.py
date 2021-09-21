import unittest
import pydash
import json

from lib.repository.statement import statement

from lib.controller.interface import Interface
from tests.mocks.operations import *


# This classe runs the implementation tests, it will execute all code from the layers bellow the controller layer.
# It will persist on the internal state, but it will be cleaned after each test.
# The main idea is to ensure that even if a bug do not get caught by the unit test suit we still will be able to get check it
class TestControllerInterface(unittest.TestCase):

    # Cleaning state after each test
    def tearDown(self):
        statement._clean_up()

    def test_account_creation_success(self):
        raw_input = pydash.map_(ACCOUNT_CREATION_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = ACCOUNT_CREATION_OUTPUT
        self.assertEqual(expected, results)

    def test_account_creation_with_account_already_initialized_violation(self):
        raw_input = pydash.map_(ACCOUNT_CREATION_FAIL_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = ACCOUNT_CREATION_FAIL_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_success(self):
        raw_input = pydash.map_(TRANSACTION_CREATION_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_CREATION_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_account_not_initialized_violation(self):
        raw_input = pydash.map_(TRANSACTION_WITH_ACCOUNT_NOT_INITIALIZED_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_WITH_ACCOUNT_NOT_INITIALIZED_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_card_not_active(self):
        raw_input = pydash.map_(TRANSACTION_WITH_CARD_NOT_ACTIVE_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_WITH_CARD_NOT_ACTIVE_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_insufficient_limit_violation(self):
        raw_input = pydash.map_(TRANSACTION_WITH_INSUFFICIENT_LIMIT_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_WITH_INSUFFICIENT_LIMIT_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_high_frequency_small_interval_violation(self):
        raw_input = pydash.map_(TRANSACTION_WITH_HIGH_FREQUENCY_SMALL_INTERVAL_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_WITH_HIGH_FREQUENCY_SMALL_INTERVAL_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_doubled_transaction_violation(self):
        raw_input = pydash.map_(TRANSACTION_WITH_DOUBLED_TRANSACTION_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_WITH_DOUBLED_TRANSACTION_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_with_multiple_violations(self):
        raw_input = pydash.map_(TRANSACTION_WITH_MULTIPLE_VIOLATIONS_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_WITH_MULTIPLE_VIOLATIONS_OUTPUT
        self.assertEqual(expected, results)

    def test_transaction_not_considering_previous_transactions_with_violations(self):
        raw_input = pydash.map_(TRANSACTION_NOT_CONSIDERING_PREVIOUS_TRANSACTION_WITH_VIOLATIONS_INPUT, lambda i: json.dumps(i))
        results = Interface().apply_operations_from_file_input(raw_input)

        expected = TRANSACTION_NOT_CONSIDERING_PREVIOUS_TRANSACTION_WITH_VIOLATIONS_OUTPUT
        self.assertEqual(expected, results)
