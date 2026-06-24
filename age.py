#***************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem
# Date:   June 23,2026
# Desc:   This program converts inches to feet and inches.
# Input:  No user input
# Output: Number of different coins
# Source: Unit 2 Lesson 4: Strings
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
#***************************************************************

def main():

    YEAR = 2026
    age = 0
    name = ""

    name = input("Enter your name: ")
    age = int(input("Enter your age " + name + ": "))

    year_born = YEAR - age

    print("Hello " + name + "! You were born in " + str(year_born) + ".")

main()