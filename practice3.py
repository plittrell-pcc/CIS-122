# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-122 Practice Problem 3
# Date:   July 2,2026
# Desc:   This program will take the dimensions of a cylinder jar and it will
#         will estimate how many gumballs it will take to fill.
# Input:  The diameter and height of the cylinder.
# Output: The approximate number of gum balls to fill cylinder.
# Source: Unit 3 Python Practice 3
# GitHub: https://github.com/plittrell-pcc/CIS-122.git
#
# ****************************************************************************

# Sample Run:
#
# Gumball Estimator!
# Enter the dimensions of a cylinder jar and I will
# tell you how many gumballs it will take to fill!
#
# Enter cylinder diameter (inches): 7
# Enter cylinder height (inches): 10
#
# The jar will hold 477 gumballs!
#
# Goodbye!

# Declare Global Constants
GUMBALL_VOLUME = 0.5236 # volume of a 1" diameter gumball
PERCENT_SOLID = 0.65    # 65% of cylinder volume contains solids (gumballs)
PI = 3.14159265         # only needed once, so no import of math module

# Declare Variables
diameter = 0.0
radius = 0.0
height = 0.0
cylinder_volume = 0.0
num_gumballs = 0

def main():

    print_welcome()

    # Get Inputs
    cylinder_diameter = get_diameter()
    cylinder_height = get_height()

    # Calculations
    radius = calc_radius(cylinder_diameter)
    usable_volume = calc_cylinder_volume(radius, cylinder_height)
    gumball_count = calc_gumballs(usable_volume)

    # Outputs
    print_results(gumball_count)


# Input Functions
def get_diameter():
    """
    Prompts the user to enter the cylinder's diameter.
    :return: float, The diameter of the cylinder.
    """
    diameter = float(input("Enter cylinder diameter (in): "))
    return diameter


def get_height():
    """
    Prompts the user to enter the cylinder's height.
    :return: float, The height of the cylinder.
    """
    height = float(input("Enter cylinder height (in): "))
    return height


# Calc Functions
def calc_radius(diameter):
    """
    Calculates the cylinder's radius.
    :param diameter: float, The diameter of the cylinder.
    :return: float, The radius of the cylinder.
    """
    radius = diameter / 2.0
    return radius


def calc_cylinder_volume(radius, height):
    """
    Calculates the cylinder's volume.
    :param radius: float, The radius of the cylinder.
    :param height: float, The height of the cylinder.
    :return: float, The cylinder's volume.
    """
    # Calculate total volume multiplied by the solid capacity percentage
    cylinder_volume = (PI * radius ** 2 * height) * PERCENT_SOLID
    return cylinder_volume


def calc_gumballs(usable_volume):
    """
    Calculates the total number of gumballs.
    :param usable_volume: float, The solid volume available in the jar.
    :return: int, The total number of gumballs.
    """
    num_gumballs = int(usable_volume / GUMBALL_VOLUME)
    return num_gumballs


# Output Functions
def print_welcome():
    """
    Prints the welcome message.
    :return: none
    """
    print("Gumball Estimator!")
    print('Enter the dimensions of a cylinder jar and I will')
    print('tell you how many 1" gumballs it will take to fill!\n')


def print_results(total_gumballs):
    """
    Prints the total number of gumballs.
    :param total_gumballs:
    :return: none
    """
    print("\nThe jar will hold", total_gumballs, "gumballs!")
    print("\nGoodbye!")


# Execute the main function to start the program
main()