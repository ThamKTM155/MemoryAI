"""
=========================================
OPERATIONS CENTER

BUILD-63A
=========================================
"""

from service.chief_operations_officer import (
    ChiefOperationsOfficer
)


class OperationsCenter:

    def __init__(self):

        self.officer = ChiefOperationsOfficer()

    def execute(self, message):

        if message is None:
            return ""

        message = str(message).strip()

        if not message:
            return "Anh chưa nhập nội dung."

        return self.officer.handle(message)


_center = OperationsCenter()


def execute(message):

    return _center.execute(message)