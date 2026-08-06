# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice 7 (Refactored)
# Date:   August 3, 2026
# Description: This program refactors Practice 5 to append user input only
#              POSITIVE integers to a list. It prompts the user to enter a
#              series of positive integers, validating input with a custom
#              module. It then iterates through the list to calculate and
#              report totals, averages, ranges, and categorical counts without
#              using built-in statistical methods.
# Inputs:      User defined series of positive integers
# Outputs:     A summary report displaying calculated statistics
# Source: Unit 7 Python Practice 7
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample Run
# __________
# Welcome to Fun with Statistics II!
#
# Enter a positive integer: 2
# Enter another? (y/n): y
#
# Enter a positive integer: 5
# Enter another? (y/n): y
#
# Enter a positive integer: 17
# Enter another? (y/n): y
#
# Enter a positive integer: 44
# Enter another? (y/n): y
#
# Enter a positive integer: 12
# Enter another? (y/n): n
#
# ------------------------------------------
#             STATISTICS REPORT
# ------------------------------------------
# Total numbers entered: 5
# Sum of numbers:        80
# Average of numbers:    16.00
# Minimum number:        2
# Maximum number:        44
# Range of numbers:      42
# ------------------------------------------
#           CATEGORICAL BREAKDOWN
# ------------------------------------------
# Even numbers:          3
# Odd numbers:           2
# ------------------------------------------
import valid

def main():
    """
    Main driver function to run program
    :return: None
    """
    display_welcome()

    # Initialize variables
    numbers_list = []
    more_numbers = 'y'


    # Data Collection Loop
    while more_numbers == 'y':
        num = get_positive_integer()
        numbers_list.append(num)
        more_numbers = get_more()

    # Processing and Output
    process_and_display_results(numbers_list)


def display_welcome():
    """
    Prints the welcome message to the user
    :return: None
    """
    print("Welcome to Fun with Statistics II!")


def get_positive_integer():
    """
    Prompts the user to input a positive integer, using valid.py
    Loops until a valid positive integer is provided.
    :return: int, valid positive integer entered by the user
    """
    while True:
        num = valid.get_integer("\nEnter a positive integer: ")
        if num > 0:
            result = num
            return result
        else:
            print("Invalid input. Please enter a positive number greater than 0.")


def get_more():
    """
    Asks the user if they want to enter another number using valid.py
    :return: str, the user's response ('y' or 'n')
    """
    response = valid.get_y_or_n("Enter another? (y/n): ")
    return response


def calculate_sum(numbers):
    """
    Repeats through list to calculate the total sum
    :param numbers: list of ints
    :return: int, calculated sum of the list
    """
    total = 0
    for num in numbers:
        total += num

    result_sum = total
    return result_sum


def calculate_min(numbers):
    """
    Repeats through list to find the minimum value
    :param numbers: list of ints
    :return: int, calculated minimum of the list
    """
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num

    result_min = minimum
    return result_min


def calculate_max(numbers):
    """
    Repeats through list to find the maximum value
    :param numbers: list of ints
    :return: int, calculated maximum of the list
    """
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num

    result_max = maximum
    return result_max


def calculate_average(total_sum, count):
    """
    Calculates the average of the numbers entered.
    :param total_sum: int, the sum of all numbers entered
    :param count: int, the total count of numbers entered
    :return: float, calculated average
    """
    avg_result = total_sum / count
    return avg_result


def calculate_range(max_num, min_num):
    """
    Calculates the range of the numbers entered.
    :param max_num: int, the maximum number inputted
    :param min_num: int, the minimum number inputted
    :return: int, calculated range
    """
    range_result = max_num - min_num
    return range_result


def calculate_categories(numbers):
    """
    Iterates through the list to count positive, negative, even, and odd numbers
    :param numbers: list of ints
    :return: tuple of ints (even_count, odd_count)
    """
    even_count = 0
    odd_count = 0

    for num in numbers:

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


def process_and_display_results(numbers):
    """
    Calculates stats from the list and displays the message
    :param numbers: list of ints, inputted numbers
    :return: None
    """
    count = len(numbers)

    if count > 0:
        # Call separated processing functions
        total_sum = calculate_sum(numbers)
        average = calculate_average(total_sum, count)
        min_num = calculate_min(numbers)
        max_num = calculate_max(numbers)
        stat_range = calculate_range(max_num, min_num)
        even_count, odd_count = calculate_categories(numbers)

        output_message(count, total_sum, average, min_num, max_num,
                       stat_range, even_count, odd_count)
    else:
        print("\nNo numbers were entered. Goodbye!")


def output_message(count, total_sum, average, min_num, max_num, stat_range, even_count, odd_count):
    """
    Prints a statistical report of results
    :param count: int, total numbers entered
    :param total_sum: int, sum of entered numbers
    :param average: float, average of entered numbers
    :param min_num: int, minimum number entered
    :param max_num: int, maximum number entered
    :param stat_range: int, calculated range of numbers
    :param even_count: int, count of even numbers
    :param odd_count: int, count of odd numbers
    :return: None
    """
    print("\n" + "-" * 42)
    print(f"{'STATISTICS REPORT':^42}")
    print("-" * 42)
    print(f"Total numbers entered: {count}")
    print(f"Sum of numbers:        {total_sum}")
    print(f"Average of numbers:    {average:.2f}")
    print(f"Minimum number:        {min_num}")
    print(f"Maximum number:        {max_num}")
    print(f"Range of numbers:      {stat_range}")
    print("-" * 42)
    print(f"{'CATEGORICAL BREAKDOWN':^42}")
    print("-" * 42)
    print(f"Even numbers:          {even_count}")
    print(f"Odd numbers:           {odd_count}")
    print("-" * 42)

# Run the program
main()