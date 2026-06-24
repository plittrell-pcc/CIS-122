#***************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem
# Date:   June 23,2026
# Desc:   Convert pennies to other coins
# Input:  No user input
# Output: Number of different coins
# Source: Lesson 3: Modulus
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
#***************************************************************

def main():
    cents = int(input('Enter number of pennies you have to convert: '))
    quarters = 0
    dimes = 0
    nickels = 0

    # calculate number of quarters and remaining pennies
    quarters = cents // 25
    cents = cents % 25

    # calculate number of dimes and remaining pennies
    dimes = cents // 10
    cents = cents % 10

    # calculate number of nickels and remaining pennies
    nickels = cents // 5
    cents = cents % 5

    # print the results
    print('Quarters:', quarters)
    print('Dimes:', dimes)
    print('Nickels:', nickels)
    print('Cents:', cents)

main()
