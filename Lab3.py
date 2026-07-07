# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Lab3
# Date:   July 6, 2026
# Desc:   Refactor Lab 2 to use functions.
#         Calculates the estimated number of calories burned during a workout
#         based on the exercise duration, refactored to use functions. Also
#         added variable calorie burn rates per feedback from Lab2
# Input:  The type of exercise and the duration in minutes.
# Output: A summary of workout activity, duration, and total calories burned.
# Source: Unit 3 Python Lab 3
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample Run
# ----------
#
# ---------- Welcome to the Personal Fitness Tracker -----------
# Track the following exercises.
#
#  (1) for Walking
#  (2) for Running
#  (3) for Cycling
#  (4) for Swimming
#
# Enter the type of exercise (1, 2, 3, 4): 2
# Enter the number of minutes you exercised: 30
# --------------------------------------------------------------
#            Workout Summary Logged Successfully!
# --------------------------------------------------------------
# Activity Type:         Running
# Calories per minute:   11.5
# Duration:              30.0 minutes
# Estimated Burn:        345.00 calories
# --------------------------------------------------------------
#               Great job staying active today!
# --------------------------------------------------------------

# Constants for calorie burn rates per minute
WALKING_RATE = 4.5
RUNNING_RATE = 11.5
CYCLING_RATE = 8.0
SWIMMING_RATE = 7.0

def main():
    print_welcome()

    # Input
    exercise_choice = get_exercise_type()
    workout_minutes = get_workout_minutes()

    # Process
    exercise_name = determine_exercise_name(exercise_choice)
    calories_per_minute = determine_calorie_rate(exercise_choice)
    total_calories_burned = calc_calories(workout_minutes, calories_per_minute)

    # Output
    print_summary(
        exercise_name, calories_per_minute, workout_minutes, total_calories_burned
    )


def print_welcome():
    """
    Print welcome message
    :return: none
    """
    print("---------- Welcome to the Personal Fitness Tracker -----------\n")


def get_exercise_type():
    """
    Get exercise type from the user
    :return: int, exercise type
    """
    print("Track the following exercises.\n")
    print(" (1) for Walking")
    print(" (2) for Running")
    print(" (3) for Cycling")
    print(" (4) for Swimming\n")

    exercise_type = int(input("Enter the type of exercise (1, 2, 3, 4): "))

    # Validate input choice
    while exercise_type not in [1, 2, 3, 4]:
        print("Invalid choice. Please select a number between 1 and 4.")
        exercise_type = int(input("Enter the type of exercise (1, 2, 3, 4): "))

    return exercise_type


def get_workout_minutes():
    """
    Get workout minutes from the user
    :return: int, workout minutes
    """
    workout_minutes = float(input("Enter the number of minutes you exercised: "))
    return workout_minutes


def determine_exercise_name(exercise_choice):
    """
    Determine exercise name
    :param exercise_choice: int, exercise type
    :return: str, exercise name result
    """

    name_result = ""

    if exercise_choice == 1:
        name_result = "Walking"
    elif exercise_choice == 2:
        name_result = "Running"
    elif exercise_choice == 3:
        name_result = "Cycling"
    elif exercise_choice == 4:
        name_result = "Swimming"

    return name_result


def determine_calorie_rate(exercise_choice):
    """
    Determine calories per minute
    :param exercise_choice: int, exercise type
    :return: float, calories per minute rate result
    """

    rate_result = 0.0

    if exercise_choice == 1:
        rate_result = WALKING_RATE
    elif exercise_choice == 2:
        rate_result = RUNNING_RATE
    elif exercise_choice == 3:
        rate_result = CYCLING_RATE
    elif exercise_choice == 4:
        rate_result = SWIMMING_RATE

    return rate_result


# noinspection PyUnusedLocal
def calc_calories(minutes, rate_per_minute):
    """
    Calculate calories per minute
    :param minutes: float, number of minutes
    :param rate_per_minute: float, calories per minute
    :return:
    """
    calculated_burn = 0.0

    calculated_burn = minutes * rate_per_minute
    return calculated_burn


def print_summary(exercise_name, cals_per_min, minutes, total_burn):
    """
    Print the summary of the exercise
    :param exercise_name: str, exercise type
    :param cals_per_min: float, calories per minute
    :param minutes: float, number of minutes
    :param total_burn: float, total burn
    :return: none
    """
    print("--------------------------------------------------------------")
    print("           Workout Summary Logged Successfully!")
    print("--------------------------------------------------------------")
    print("Activity Type:        ", exercise_name)
    print("Calories per minute:  ", cals_per_min)
    print("Duration:             ", minutes, "minutes")
    print("Estimated Burn:       ", format(total_burn, ".2f"), "calories")
    print("--------------------------------------------------------------")
    print("              Great job staying active today!")
    print("--------------------------------------------------------------")


# Run Program
main()
