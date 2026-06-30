# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Lab2
# Date:   June 30,2026
# Desc:   Calculates the estimated number of calories burned during a workout
#         based on the exercise duration.
# Input:  The type of exercise and the duration in minutes.
# Output: A summary of workout activity, duration, and total calories burned.
# Source: Unit 2 Python Lab 2
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample Run
# ----------
#
# ---------- Welcome to the Personal Fitness Tracker -----------
# Enter the type of exercise (e.g., Running, Cycling, Swimming): Running
# Enter the number of minutes you exercised: 30
#
# --------------------------------------------------------------
#            Workout Summary Logged Successfully!
# --------------------------------------------------------------
# Activity Type:     Running
# Duration:          30 minutes
# Estimated Burn:    258.00 calories
# --------------------------------------------------------------
#               Great job staying active today!
# --------------------------------------------------------------
#

# Average calories burned per minute for a moderate workout
CALORIES_PER_MINUTE = 8.6

print("---------- Welcome to the Personal Fitness Tracker -----------")

# Get the name of the exercise and duration of workout
exercise_type = input("Enter the type of exercise (e.g., Running, Cycling, Swimming): ")
workout_minutes = float(input("Enter the number of minutes you exercised: "))

# Multiply the minutes by our constant burn rate
total_calories_burned = workout_minutes * CALORIES_PER_MINUTE

# Print output
print("--------------------------------------------------------------")
print("           Workout Summary Logged Successfully!")
print("--------------------------------------------------------------")
print("Activity Type:    ", exercise_type)
print("Duration:         ", workout_minutes, "minutes")
print("Estimated Burn:   ", format(total_calories_burned, ".2f"), "calories")
print("--------------------------------------------------------------")
print("              Great job staying active today!")
print("--------------------------------------------------------------")
