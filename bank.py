from dataclasses import dataclass
from datetime import datetime
import bisect

# Note:
#
# We don't store the current balance anywhere. Instead, we store a
# list of operations, and we compute the current balance from the list
# of stored operations.
#
# It may seems costly to walk the list every time, but we can truncate
# the history whenever we want!
#
# In the same vein, to create an account we just create an initial deposit
# and add it to the list


# Note: the same class is used for withdrawals and deposits,
# we just use negative amounts for withdrawals
@dataclass(order=True, frozen=True)
class Operation:
    date: str
    amount: int


class Operations:
    def __init__(self):
        self.operations = []

    def insert_operation(self, operation):
        # It's important to keep operations sorted
        bisect.insort(self.operations, operation)

    def __iter__(self):
        return iter(self.operations)


@dataclass(order=True, frozen=True)
class HistoryLine:
    date: datetime
    amount: int
    balance: int


class History:
    def __init__(self):
        self.lines = []

    def append_line(self, line):
        bisect.insort(self.lines, line)

    def as_text(self):
        res = ""
        for line in reversed(self.lines):
            res += f"{line.date.strftime('%Y-%m-%d')} {line.amount} {line.balance}\n"
        return res


class Account:
    def __init__(self):
        self.operations = Operations()

    def record_deposit(self, amount, *, date):
        operation = Operation(date=date, amount=amount)
        self.operations.insert_operation(operation)

    def record_withdrawal(self, amount, *, date):
        operation = Operation(date=date, amount=-amount)
        self.operations.insert_operation(operation)

    @property
    def balance(self):
        result = 0
        for operation in self.operations:
            result += operation.amount
        return result

    @property
    def history(self):
        res = History()
        balance = 0
        for operation in self.operations:
            balance += operation.amount
            line = HistoryLine(
                amount=operation.amount, date=operation.date, balance=balance
            )
            res.append_line(line)
        return res
