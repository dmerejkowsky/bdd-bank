# The Bank Kata

You'll find here my attempt at solving the bank kata.

Inspired by : https://github.com/iAmDorra/BankKata_and_cqrs

Some notes:

* I'm using `dataclass(frozen=True)` for Value Objects

* Implementation is in `bank.py` with a few helpful comments

* I'm using [pytest](https://pytest.org) and [pytest-
  bdd](https://pytest-bdd.readthedocs.io/en/latest/) to execute run the
  scenarios stored in the `tests/features/` directory

* I tried to use only calisthenics objects

* You can find a rough logs of the steps I took in `log.txt`

## Running the tests

Install [poetry](https://python-poetry.org/)

```
poetry install
poetry run pytest
```
