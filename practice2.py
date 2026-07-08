# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem 2
# Date:   June 29,2026
# Desc:   This program calculates the cost of gas to drive
#         20, 50, and 500 miles.
# Input:  The car's mpg and the cost of 1 gallon of gas.
# Output: The gas cost for 20 miles, 75 miles, and 500 miles.
# Source: Unit 2 Python Practice 2
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample run
# ----------
# Enter your cars MPG: 27
# Enter the current cost of 1 gallon of gas: 4.25
#
# The cost of driving 20 miles is $3.15
# The cost of driving 75 miles is $11.81
# The cost of driving 500 miles is $78.70

# Declaring variables use in program.
mpg = 0.0
gas_price = 0.0
cost_20 = 0.0
cost_75 = 0.0
cost_500 = 0.0

# Prompt the user for MPG and gas price
mpg = float(input("Enter the car's MPG: "))
gas_price = float(input("Enter the gas price per gallon: "))

# Calculate the gas cost for each specific distance
# Formula used: (Distance / MPG) * Gas Price
cost_20 = (20 / mpg) * gas_price
cost_75 = (75 / mpg) * gas_price
cost_500 = (500 / mpg) * gas_price

# Output the results
print("The cost of driving 20 miles is $", format(cost_20, '.2f'), sep="")
print("The cost of driving 75 miles is $", format(cost_75, '.2f'), sep="")
print("The cost of driving 500 miles is $", format(cost_500, '.2f'), sep="")
