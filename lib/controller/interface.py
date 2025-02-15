import json
import pydash
from lib.business.account import AccountAuthorizer
from lib.business.transaction import TransactionAuthorizer


class Interface:
    def __init__(self):
        super().__init__()
        self.authorizers = {
            "account": AccountAuthorizer,
            "transaction": TransactionAuthorizer
        }

    @staticmethod
    def _convert_input_file_line_to_dict(line):
        return json.loads(line)

    @staticmethod
    def get_specific_authorizer_by_operation(operation, authorizers):
        for key, authorizer in authorizers.items():
            if key in operation:
                return authorizer()

    def apply_operations_from_file_input(self, file_input):
        operations = pydash.map_(file_input, self._convert_input_file_line_to_dict)
        outputs = pydash.map_(operations, lambda operation: self.get_specific_authorizer_by_operation(operation, self.authorizers)
                              .review_operation(operation))

        for output in outputs:
            print(json.dumps(output))

        return outputs
