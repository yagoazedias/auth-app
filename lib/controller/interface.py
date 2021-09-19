import json
import pydash
from lib.business.Authorizer import Authorizer


class Interface:

    @staticmethod
    def _convert_input_file_line_to_dict(line):
        return json.loads(line)

    def apply_operations_from_file_input(self, file_input):
        operations = pydash.map_(file_input, self._convert_input_file_line_to_dict)
        outputs = pydash.map_(operations, lambda operation: Authorizer.get_specific_operator_by_operation(operation)
                              .review_operation(operation))

        for output in outputs:
            print(output)
