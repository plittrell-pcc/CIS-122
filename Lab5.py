# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Lab4
# Date:   July 11, 2026
# Desc:   Add a while loop to your main() function to execute your program
#         until the user wants to quit.
#
#         Updated to add custom exercise calculation and program asks use
#         if they want to calculate any other exercises. Also, reformated
#         so of the output sections
#
#         Calculates the estimated number of calories burned during a workout
#         based on the exercise duration, refactored to use functions. Also
#         added variable calorie burn rates per feedback from Lab2. Includes
#         functionality for unlisted custom exercises.
#
# Input:  The type of exercise and the duration in minutes.
# Output: A summary of workout activity, duration, and total calories burned.
# Source: Unit 5 Python Lab 5
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
# ****************************************************************************
#
# Sample Run
# __________
#
# ------------------------------------------
#  Welcome to the Personal Fitness Tracker
# ------------------------------------------
# Track the following exercises.
#
#  (1) for Walking
#  (2) for Running
#  (3) for Cycling
#  (4) for Swimming
#  (5) for Custom Exercise
#
# Enter the type of exercise (1, 2, 3, 4, 5): 5
# Enter the name of your custom exercise: Push-Ups
# Enter the calories burned per minute for this exercise: 7
# Enter the number of minutes you exercised: 15
#
# --------------------------------------------------------------
#              Workout Summary Logged Successfully!
# --------------------------------------------------------------
#
# Activity Type:         Push-Ups
# Calories per minute:   7.0
# Duration:              15.0 minutes
# Estimated Burn:        105.00 calories
#
# --------------------------------------------------------------
#                Great job staying active today!
# --------------------------------------------------------------
#
# Would you like to calculate another exercise? (y/n): n
#
# --------------------------------------------------------------
#       Thank you for using the Personal Fitness Tracker.
# --------------------------------------------------------------
#


# Constants for calorie burn rates per minute
WALKING_RATE = 4.5
RUNNING_RATE = 11.5
CYCLING_RATE = 8.0
SWIMMING_RATE = 7.0


def main():
    continue_program = 'y'

    while continue_program.lower() == 'y':
        print_welcome()

        # Input
        exercise_choice = get_exercise_type()

        # Process based on custom vs standard exercise
        if exercise_choice == 5:
            exercise_name = get_custom_name()
            calories_per_minute = get_custom_rate()
        else:
            exercise_name = determine_exercise_name(exercise_choice)
            calories_per_minute = determine_calorie_rate(exercise_choice)

        workout_minutes = get_workout_minutes()
        total_calories_burned = calc_calories(workout_minutes, calories_per_minute)

        # Determine the motivation message
        motivation_message = determine_motivation(total_calories_burned)

        # Output
        print_summary(
            exercise_name, calories_per_minute, workout_minutes, total_calories_burned, motivation_message
        )

        # Prompt to continue loop
        continue_program = get_keep_going()

    # Exit message
    print_thank_you()


def print_welcome():
    """
    Print welcome message
    :return: none
    """
    print("\n" + "-" * 42)
    print(f"{'Welcome to the Personal Fitness Tracker':^42}")
    print("-" * 42)

def get_exercise_type():
    """
    Get exercise type from the user
    :return: int, exercise type
    """
    print("Track the following exercises.\n")
    print(" (1) for Walking")
    print(" (2) for Running")
    print(" (3) for Cycling")
    print(" (4) for Swimming")
    print(" (5) for Custom Exercise\n")

    exercise_type = int(input("Enter the type of exercise (1, 2, 3, 4, 5): "))

    # Validate input choice
    while exercise_type not in [1, 2, 3, 4, 5]:
        print("Invalid choice. Please select a number between 1 and 5.")
        exercise_type = int(input("Enter the type of exercise (1, 2, 3, 4, 5): "))

    return exercise_type


def get_custom_name():
    """
    Get the name of the unlisted exercise
    :return: str, custom exercise name
    """
    name = input("Enter the name of your custom exercise: ")
    return name


def get_custom_rate():
    """
    Get the calorie burn rate for the unlisted exercise
    :return: float, custom calorie burn rate
    """
    rate_input = float(input("Enter the calories burned per minute for this exercise: "))
    return rate_input


def get_workout_minutes():
    """
    Get workout minutes from the user
    :return: float, workout minutes
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


def calc_calories(minutes, rate_per_minute):
    """
    Calculate total calories burned
    :param minutes: float, number of minutes
    :param rate_per_minute: float, calories per minute
    :return: float, calculated burn
    """
    calculated_burn = 0.0

    calculated_burn = minutes * rate_per_minute
    return calculated_burn


def print_summary(exercise_name, cals_per_min, minutes, total_burn, motivation):
    """
    Print the summary of the exercise
    :param exercise_name: str, exercise type
    :param cals_per_min: float, calories per minute
    :param minutes: float, number of minutes
    :param total_burn: float, total burn
    :param motivation: str, custom motivation message
    :return: none
    """

    message = "Workout Summary Logged Successfully!"

    print("\n" + "-" * 62)
    print(message.center(62))
    print("-" * 62 + "\n")
    print("Activity Type:        ", exercise_name)
    print("Calories per minute:  ", cals_per_min)
    print("Duration:             ", minutes, "minutes")
    print("Estimated Burn:       ", format(total_burn, ".2f"), "calories")
    print("\n" + "-" * 62)
    print(motivation.center(62))
    print("-" * 62 + "\n")


def determine_motivation(total_burn):
    """
    Determine a motivational message based on calories burned
    :param total_burn: float, total calories burned
    :return: str, motivational message
    """

    message = ""

    if total_burn >= 500:
        message = "Incredible workout! You are a machine!"
    elif total_burn >= 300:
        message = "Awesome job pushing yourself today!"
    elif total_burn > 100:
        message = "Great job staying active today!"
    else:
        message = "Every little bit counts!"

    return message


def get_keep_going():
    """
    Ask the user if they want to calculate another exercise
    :return: str, user choice
    """
    choice = input("Would you like to calculate another exercise? (y/n): ")
    return choice


def print_thank_you():
    """
    Print an exit message when the program concludes
    :return: none
    """
    thank_you_message = "Thank you for using the Personal Fitness Tracker."

    print("\n" + "-" * 62)
    print(thank_you_message.center(62))
    print("-" * 62 + "\n")


# Run Program
main()