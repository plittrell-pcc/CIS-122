# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice 5
# Date:   July 9, 2026
# Description: This program prompts the user to enter a series of integers
#              until they choose to stop. It tracks the inputs and calculates
#              statistics and reports totals, averages, ranges, and categorical
#              counts.
# Inputs:      User defined series of integers
# Outputs:     A summary report displaying calculated statistics
# Source: Unit 5 Python Practice 5
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Welcome to Fun with Statistics!
#
# Enter an integer: 1
# Enter another? (y/n): y
#
# Enter an integer: 6
# Enter another? (y/n): y
#
# Enter an integer: -4
# Enter another? (y/n): y
#
# Enter an integer: 23
# Enter another? (y/n): y
#
# Enter an integer: -45
# Enter another? (y/n): n
#
# ------------------------------------------
#             STATISTICS REPORT
# ------------------------------------------
# Total numbers entered: 5
# Sum of numbers:        -19
# Average of numbers:    -3.80
# Minimum number:        -45
# Maximum number:        23
# Range of numbers:      68
# ------------------------------------------
#           CATEGORICAL BREAKDOWN
# ------------------------------------------
# Positive numbers:      3
# Negative numbers:      2
# Even numbers:          2
# Odd numbers:           3
# ------------------------------------------

def main():
    """
    Main driver function to run program
    :return: None
    """
    display_welcome()

    # Initialize variables
    more_numbers = 'y'
    count = 0
    total_sum = 0
    min_num = 0
    max_num = 0
    pos_count = 0
    neg_count = 0
    even_count = 0
    odd_count = 0

    # Data Collection Loop
    while more_numbers.lower() == 'y':
        num = get_number()

        # Pass variables to calculator
        (count, total_sum, min_num, max_num,
         pos_count, neg_count, even_count, odd_count) = calculate_stats(
            count, total_sum, min_num, max_num,
            pos_count, neg_count, even_count, odd_count, num)

        more_numbers = get_more()

    # Processing and Output
    process_and_display_results(count, total_sum, min_num, max_num,
                                pos_count, neg_count, even_count, odd_count)


def display_welcome():
    """
    Prints the welcome message to the user
    :return: None
    """
    print("Welcome to Fun with Statistics!")


def process_and_display_results(count, total_sum, min_num, max_num, pos_count, neg_count, even_count, odd_count):
    """
    Calculates stats, and output message
    :param count: int, total numbers entered
    :param total_sum: int, sum of entered numbers
    :param min_num: int, minimum number entered
    :param max_num: int, maximum number entered
    :param pos_count: int, count of positive numbers
    :param neg_count: int, count of negative numbers
    :param even_count: int, count of even numbers
    :param odd_count: int, count of odd numbers
    :return: None
    """
    if count > 0:
        average = calculate_average(total_sum, count)
        stat_range = calculate_range(max_num, min_num)

        output_message(count, total_sum, average, min_num, max_num,
                       stat_range, pos_count, neg_count, even_count, odd_count)
    else:
        print("\nNo numbers were entered. Goodbye!")


def get_number():
    """
    Prompts the user to input integer
    :return: int, integer entered by the user
    """
    num = int(input("\nEnter an integer: "))
    return num


def get_more():
    """
    Asks the user if they want to enter another number
    :return: str, the user's response ('y' or 'n')
    """
    more = input("Enter another? (y/n): ")
    return more


def calculate_stats(count, total_sum, min_num, max_num, pos_count, neg_count, even_count, odd_count, num):
    """
    Updates running counts, totals, minimums, maximums, and category counts
    :param count: int, current count of numbers
    :param total_sum: int, current sum of numbers
    :param min_num: int, current minimum number
    :param max_num: int, current maximum number
    :param pos_count: int, current count of positive numbers
    :param neg_count: int, current count of negative numbers
    :param even_count: int, current count of even numbers
    :param odd_count: int, current count of odd numbers
    :param num: int, the latest number entered by the user
    :return: ints, updated statistical tracking variables
    """
    # Update Min/Max
    if count == 0:
        min_num = num
        max_num = num
    else:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    # Update Positive/Negative Counts
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1

    # Update Even/Odd Counts
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # Update Running Sum and Total Count
    updated_sum = total_sum + num
    updated_count = count + 1

    return (updated_count, updated_sum, min_num, max_num,
            pos_count, neg_count, even_count, odd_count)


def calculate_average(total_sum, count):
    """
    Calculates the average of the numbers entered
    :param total_sum: int, the sum of all numbers entered
    :param count: int, the total count of numbers entered
    :return: float, calculated average
    """
    avg_result = total_sum / count
    return avg_result


def calculate_range(max_num, min_num):
    """
    Calculates the range of the numbers entered
    :param max_num: int, the maximum number inputted
    :param min_num: int, the minimum number inputted
    :return: int, calculated range
    """
    range_result = max_num - min_num
    return range_result


def output_message(count, total_sum, average, min_num, max_num, stat_range, pos_count, neg_count, even_count,
                   odd_count):
    """
    Prints a statistical report of results
    :param count: int, total numbers entered
    :param total_sum: int, sum of entered numbers
    :param average: float, average of entered numbers
    :param min_num: int, minimum number entered
    :param max_num: int, maximum number entered
    :param stat_range: int, calculated range of numbers
    :param pos_count: int, count of positive numbers
    :param neg_count: int, count of negative numbers
    :param even_count: int, count of even numbers
    :param odd_count: int, count of odd numbers
    :return: None, no return value
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
    print(f"Positive numbers:      {pos_count}")
    print(f"Negative numbers:      {neg_count}")
    print(f"Even numbers:          {even_count}")
    print(f"Odd numbers:           {odd_count}")
    print("-" * 42)


# Run the program
main()