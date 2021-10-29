Feature: Bank Account
  An account where you can make deposits and withdraws.

  Scenario: Creating a bank acount with an initial balance
    When I create a bank account with an initial balance of 200
    Then My bank account has a balance of 200

  Scenario: Making a deposit
    Given I have a bank account with a balance of 200
    When I make a deposit of 50
    Then My bank account has a balance of 250

  Scenario: Making a withdrawal
    Given I have a bank account with a balance of 200
    When I make a withdrawal of 10
    Then My bank account has a balance of 190

  Scenario: Seeing the history
    Given My bank account had a balance of 200 on 2020-12-31
    And I made a withdrawal of 10 on 2021-01-01
    And I made a deposit of 20 on 2021-01-02
    And I made a withdrawal of 5 on 2021-01-03
    Then I see the following history:
        2021-01-03 -5 205
        2021-01-02 20 210
        2021-01-01 -10 190
        2020-12-31 200 200
