//***************************************************************
//
// Author: Paul Littrell
// Lab:    CIS-122 Practice Problem (Converted to C++)
// Date:   June 23, 2026
// Desc:   This program calculates a user's birth year.
//         but in c++ as a test
// Input:  User's name and age
// Output: Hello message with calculated birth year
// Source: Unit 2 Lesson 4: Strings
// GitHub: https://github.com/plittrell-pcc/CIS-122.git
//
//***************************************************************

#include <iostream>
#include <string>

int main() {
    const int YEAR = 2026;
    int age = 0;
    std::string name = "";

    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    std::cout << "Enter your age " << name << ": ";
    std::cin >> age;

    int year_born = YEAR - age;

    std::cout << "Hello " << name << "! You were born in " << year_born << ".\n";

    return 0;
}