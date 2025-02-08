import subprocess
import unittest


class TestIntegration(unittest.TestCase):

    def setUp(self):
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    def read_expected_output(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def run_authorize_script(self, input_file):
        with open(input_file, "r") as file:
            result = subprocess.run(
                ["python3", "authorize.py"],
                stdin=file,
                stdout=subprocess.PIPE,
                text=True,
                check=True
            )
        return result.stdout

    def test_account_creation_success(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_account_creation_success.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_account_creation_success.txt")
        self.assertEqual(expected_output, output)

    def test_account_creation_with_account_already_initialized_violation(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_account_creation_with_account_already_initialized_violation.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_account_creation_with_account_already_initialized_violation.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_success(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_success.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_success.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_account_not_initialized_violation(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_account_not_initialized_violation.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_account_not_initialized_violation.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_card_not_active(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_card_not_active.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_card_not_active.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_insufficient_limit_violation(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_insufficient_limit_violation.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_insufficient_limit_violation.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_high_frequency_small_interval_violation(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_high_frequency_small_interval_violation.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_high_frequency_small_interval_violation.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_doubled_transaction_violation(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_doubled_transaction_violation.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_doubled_transaction_violation.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_with_multiple_violations(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_with_multiple_violations.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_with_multiple_violations.txt")
        self.assertEqual(expected_output, output)

    def test_transaction_not_considering_previous_transactions_with_violations(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_transaction_not_considering_previous_transactions_with_violations.txt")
        output = self.run_authorize_script("tests/integration/samples/input_file_transaction_not_considering_previous_transactions_with_violations.txt")
        self.assertEqual(expected_output, output)
