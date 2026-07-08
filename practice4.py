# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem 4
# Date:   July 8, 2026
# Desc:   Program to prompt a user for their total change as a decimal and
#         output the change using the fewest coins, one coin type per line
# Input:  Total change in decimal (e.g., 1.45)
# Output: Print change in number dollars,quarters,dimes,nickles and pennies
# Source: Unit 4 Python Practice 4
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample runs
# -----------
# Enter total change (e.g., 1.45): 0
# No Change.
#
# Enter total change (e.g., 1.45): .26
# 1 Quarter
# 1 Penny
#
# Enter total change (e.g., 1.45): 1.55
# 1 Dollar
# 2 Quarters
# 1 Nickel

def main():
    """
    Main function to manage the input, process, and output functions.
    :return: none
    """
    #Get input
    total_cents = get_input()

    #Process calculations with multiple returns
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = calculate_change(total_cents)

    #Output
    output_change(total_cents, num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)


def get_input():
    """
    Prompts the user to enter their total change as a decimal (e.g., 1.45)
    :Return: int, The user's input amount converted to total cents
    """
    amount = 0.0
    cents = 0

    amount = float(input("Enter total change (e.g., 1.45): "))

    # Convert to cents by multiplying by 100 then convert to an integer
    cents = int(amount * 100)

    return cents


def calculate_change(cents):
    """
    Calculates the exact change using the fewest coins possible
    :Param cents: int, The total amount of change to calculate
    :Return: int, dollars, quarters, dimes, nickels, pennies
    """

    remaining = 0
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    # Calculate dollars
    dollars = cents // 100
    remaining = cents % 100

    # Calculate quarters
    quarters = remaining // 25
    remaining = remaining % 25

    # Calculate dimes
    dimes = remaining // 10
    remaining = remaining % 10

    # Calculate nickels
    nickels = remaining // 5
    remaining = remaining % 5

    # Calculate pennies
    pennies = remaining

    return dollars, quarters, dimes, nickels, pennies


def output_change(total_cents, dollars, quarters, dimes, nickels, pennies):
    """
    Outputs the calculated change with correct singular/plural naming
    :Param total_cents: int, The original input
    :Param dollars: int, Number of dollars
    :Param quarters: int, Number of quarters
    :Param dimes: int, Number of dimes
    :Param nickels: int, Number of nickels
    :Param pennies: int, Number of pennies
    :Return: None
    """
    # Handle no change
    if total_cents <= 0:
        print("No Change.")
    else:
        # Handle correct singular/plural naming
        if dollars > 0:
            if dollars == 1:
                print(f"{dollars} Dollar")
            else:
                print(f"{dollars} Dollars")

        if quarters > 0:
            if quarters == 1:
                print(f"{quarters} Quarter")
            else:
                print(f"{quarters} Quarters")

        if dimes > 0:
            if dimes == 1:
                print(f"{dimes} Dime")
            else:
                print(f"{dimes} Dimes")

        if nickels > 0:
            if nickels == 1:
                print(f"{nickels} Nickel")
            else:
                print(f"{nickels} Nickels")

        if pennies > 0:
            if pennies == 1:
                print(f"{pennies} Penny")
            else:
                print(f"{pennies} Pennies")


# Run the program
main()