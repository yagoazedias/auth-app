import os
import unittest


class TestIntegration(unittest.TestCase):

    def test_account_creation_success(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_account_creation_success.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_account_creation_success.txt').read()

        self.assertEqual(expected_output, output)

    def test_account_creation_with_account_already_initialized_violation(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_account_creation_with_account_already_initialized_violation.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_account_creation_with_account_already_initialized_violation.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_success(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_success.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_success.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_account_not_initialized_violation(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_account_not_initialized_violation.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_account_not_initialized_violation.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_card_not_active(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_card_not_active.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_card_not_active.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_insufficient_limit_violation(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_insufficient_limit_violation.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_insufficient_limit_violation.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_high_frequency_small_interval_violation(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_high_frequency_small_interval_violation.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_high_frequency_small_interval_violation.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_doubled_transaction_violation(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_doubled_transaction_violation.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_doubled_transaction_violation.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_with_multiple_violations(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_with_multiple_violations.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_with_multiple_violations.txt').read()

        self.assertEqual(expected_output, output)

    def test_transaction_not_considering_previous_transactions_with_violations(self):
        os.system("pip install -r ../requirements.txt")
        expected_output_file = open("integration/expected/output_file_transaction_not_considering_previous_transactions_with_violations.txt", "r")
        expected_output = expected_output_file.read()
        expected_output_file.close()

        output = os.popen('python3 ../authorize.py < integration/samples/input_file_transaction_not_considering_previous_transactions_with_violations.txt').read()

        self.assertEqual(expected_output, output)
