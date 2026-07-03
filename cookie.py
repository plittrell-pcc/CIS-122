# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem
# Date:   June 29,2026
# Desc:   This program calculates calories from eating cookies
# Input:  The number of cookies eaten
# Output: Total calories of the cookies eaten
# Source: Unit 2 Python Practice
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************


# Declare integer cookies
# Declare float calories
# cookies = 0     // I prefer to declare the type while setting the variable
# calories = 0.0  // I prefer to declare the type while setting the variable

#Set serving size
COOKIES_PER_SERVING = 4
CALORIES_PER_SERVING = 300

# Prompt for cookies eaten and store into cookies
cookies = int(input('Enter number of cookies eaten:'))

# Calculate calories = cookies * 300 / 4
calories = float(cookies * CALORIES_PER_SERVING / COOKIES_PER_SERVING)

# Display calories eaten
print ('Calories eaten:', calories)
