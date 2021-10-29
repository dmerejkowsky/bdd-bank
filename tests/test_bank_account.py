import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from bank import Account, Operation
from datetime import datetime

scenarios("features")


@when(
    parsers.parse("I create a bank account with an initial balance of {amount:d}"),
    target_fixture="account",
)
@given(
    parsers.parse("I have a bank account with a balance of {amount:d}"),
    target_fixture="account",
)
def initial_account_with_balance(
    amount,
):
    res = Account()
    res.record_deposit(amount, date=datetime.now())
    return res


@when(parsers.parse("I make a deposit of {amount:d}"))
def deposit(account, amount):
    account.record_deposit(amount, date=datetime.now())


@when(parsers.parse("I make a withdrawal of {amount:d}"))
def withdraw(account, amount):
    account.record_withdrawal(amount, date=datetime.now())


@then(parsers.parse("My bank account has a balance of {amount:d}"))
def assert_account_balance(account, amount):
    assert account.balance == amount


@given(
    parsers.parse("My bank account had a balance of {amount:d} on {date}"),
    target_fixture="account",
)
def account_with_operations(amount, date):
    date = datetime.strptime(date, "%Y-%m-%d")
    account = Account()
    account.record_deposit(amount, date=date)
    return account


@given(
    parsers.parse("I made a withdrawal of {amount:d} on {date}"),
)
def withdraw_on(account, amount, date):
    date = datetime.strptime(date, "%Y-%m-%d")
    operation = Operation(amount=-amount, date=date)
    account.operations.insert_operation(operation)


@given(
    parsers.parse("I made a deposit of {amount:d} on {date}"),
)
def deposit_on(account, amount, date):
    date = datetime.strptime(date, "%Y-%m-%d")
    operation = Operation(amount=amount, date=date)
    account.operations.insert_operation(operation)


@then(parsers.parse("I see the following history:\n{history_lines}"))
def history(account, history_lines):
    actual = account.history.as_text()
    assert actual.strip() == history_lines.strip()
