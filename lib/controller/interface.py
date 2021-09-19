import json
import pydash
from lib.business.account import AccountAuthorizer
from lib.business.transaction import TransactionAuthorizer


class Interface:

    @staticmethod
    def _convert_input_file_line_to_dict(line):
        return json.loads(line)

    @staticmethod
    def get_specific_authorizer_by_operation(operation):
        if "account" in operation:
            return AccountAuthorizer()
        elif "transaction" in operation:
            return TransactionAuthorizer()

    def apply_operations_from_file_input(self, file_input):
        operations = pydash.map_(file_input, self._convert_input_file_line_to_dict)
        outputs = pydash.map_(operations, lambda operation: self.get_specific_authorizer_by_operation(operation)
                              .review_operation(operation))

        for output in outputs:
            print(output)
