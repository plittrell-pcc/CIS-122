# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice 6
# Date:   July 14, 2026
# Description: This program simulates a basic banking system for PCC Credit
#              Union. It uses menus to allow users to make deposits,
#              withdraw funds, and view their current balance
# Inputs:      Menu choices, deposit amounts, and withdrawal amounts
#              validated by the valid.py module
# Outputs:     Menu options, current account balances formatted as currency,
#              and a goodbye message
# Source: Unit 6 Python Practice 6
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample Run
# ----------
#
# Welcome to PCC Credit Union
#
# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit
#
# Enter choice: 1
# Account balance: $ 0.00
#
# Enter choice: 2
# Enter deposit amount $ 150.60
#
# Enter choice: 1
# Account balance: $ 150.60
#
# Enter choice: 3
# Enter withdraw amount $ 10.23
#
# Enter choice: 1
# Account balance: $ 140.37
#
# Enter choice: 4
#
# Thank you for using PCC Credit Union!

import valid as v

# Constant for Main Menu
QUIT = 4

def main():
    """
    Runs the main banking program loop
    :return: none
    """
    choice = 0
    balance = 0.0
    deposit = 0.0
    withdraw = 0.0

    print("Welcome to PCC Credit Union")

    print_menu()

    while choice != QUIT:
        choice = get_choice()

        if choice == 1:
            print_balance(balance)

        elif choice == 2:
            deposit = get_deposit_amt()
            balance = calc_deposit(balance, deposit)

        elif choice == 3:
            withdraw = get_withdraw_amt(balance)
            balance = calc_withdraw(balance, withdraw)

    print("\nThank you for using PCC Credit Union!")


def get_choice():
    """
    Prompts the user for a menu choice and validates it
    :return: int, a valid menu choice between 1 and 4
    """
    choice = 0
    result = 0

    choice = v.get_integer("\nEnter choice: ")

    while choice < 1 or choice > 4:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        choice = v.get_integer("\nEnter choice: ")

    result = choice
    return result


def get_deposit_amt():
    """
    Prompts the user for a deposit amount and validates it
    :return: float, a valid deposit amount greater than or equal to 0
    """
    amount = 0.0
    result = 0.0

    amount = v.get_real("Enter deposit amount $ ")

    while amount < 0:
        print("Deposit amount cannot be a negative number.")
        amount = v.get_real("Enter deposit amount $ ")

    result = amount
    return result


def get_withdraw_amt(balance):
    """
    Prompts the user for a withdrawal amount and validates it
    :param balance: float, the current account balance
    :return: float, a valid withdrawal amount >= 0 and <= the current balance
    """
    amount = 0.0
    result = 0.0

    amount = v.get_real("Enter withdraw amount $ ")

    while amount < 0 or amount > balance:
        print(f"Invalid amount. Must be >= 0 and <= your balance (${format(balance, '.2f')}).")
        amount = v.get_real("Enter withdraw amount $ ")

    result = amount
    return result


def calc_deposit(balance, deposit_amt):
    """
    Calculates the new balance after making a deposit
    :param balance: float, the current account balance
    :param deposit_amt: float, the amount to deposit
    :return: float, the updated account balance
    """
    new_balance = 0.0

    new_balance = balance + deposit_amt
    return new_balance


def calc_withdraw(balance, withdraw_amt):
    """
    Calculates the new balance after making a withdrawal
    :param balance: float, the current account balance
    :param withdraw_amt: float, the amount to withdraw
    :return: float, the updated account balance
    """
    new_balance = 0.0

    new_balance = balance - withdraw_amt
    return new_balance


def print_menu():
    """
    Prints the menu to view balance, make deposit, or withdraw funds
    :return: none
    """
    print("\n1. View balance")
    print("2. Make deposit")
    print("3. Withdraw funds")
    print("4. Quit")


def print_balance(balance):
    """
    Prints the current account balance
    :param balance: float, the current account balance
    :return: none
    """
    print("Account balance: $", format(balance, ".2f"))


# Run Program
main()