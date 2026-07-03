# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem
# Date:   June 23,2026
# Desc:   This program converts inches to feet and inches.
# Input:  No user input
# Output: Number of different coins
# Source: Unit 2 Lesson 3: Modulus
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

def main():

    # print welcome message
    print('Welcome')
    print('This program converts inches to feet and inches. \n\n')

    # get number of inches from the user
    inches1 = int(input('Enter number of inches: '))

    # convert the inches to feet and inches
    feet = inches1 // 12
    inches2 = inches1 % 12

    # output the conversion
    print (f'{inches1} equals {feet} feet and {inches2} inches')

main()
