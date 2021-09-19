from datetime import datetime
from lib.constants.time import TIME_FORMAT


def get_datetime_from_operation_time(operation):
    return datetime.strptime(operation["transaction"]["time"], TIME_FORMAT)
