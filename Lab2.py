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

# Declare variables
CALORIES_PER_MINUTE = 8.6
exercise_type = 0
workout_minutes = 0.0
total_calories_burned = 0.0

print("---------- Welcome to the Personal Fitness Tracker -----------")

# Get the name of the exercise and duration of workout

print("Enter the type of exercise.\n")
print("Enter (1) for Walking")
print("Enter (2) for Running")
print("Enter (3) for Cycling")
print("Enter (4) for Swimming\n")

# Get the initial input for exercise type
exercise_type = int(input("Enter the type of exercise (1, 2, 3, 4): "))

# Loop as long as the input is NOT one of the valid options
while exercise_type not in [1, 2, 3, 4]:
    print("Invalid choice. Please select a number between 1 and 4.")
    exercise_type = int(input("Enter the type of exercise (1, 2, 3, 4): "))

# The if-elif-else section to handle input
if exercise_type == 1:
    print("You selected: Walking")
    exercise_type = "Walking"
    CALORIES_PER_MINUTE = 4.5

elif exercise_type == 2:
    print("You selected: Running")
    exercise_type = "Running"
    CALORIES_PER_MINUTE = 11.5

elif exercise_type == 3:
    print("You selected: Cycling")
    exercise_type = "Cycling"
    CALORIES_PER_MINUTE = 8.0

elif exercise_type == 4:
    print("You selected: Swimming")
    exercise_type = "Swimming"
    CALORIES_PER_MINUTE = 7.0

else:
    # This is a safety net, though our while loop prevents ever reaching it
    print("Unknown exercise type.")

workout_minutes = float(input("Enter the number of minutes you exercised: "))

# Multiply the minutes by our constant burn rate
total_calories_burned = workout_minutes * CALORIES_PER_MINUTE

# Print output
print("--------------------------------------------------------------")
print("           Workout Summary Logged Successfully!")
print("--------------------------------------------------------------")
print("Activity Type:        ", exercise_type)
print("Calories per minute:  ", CALORIES_PER_MINUTE)
print("Duration:             ", workout_minutes, "minutes")
print("Estimated Burn:       ", format(total_calories_burned, ".2f"), "calories")
print("--------------------------------------------------------------")
print("              Great job staying active today!")
print("--------------------------------------------------------------")
