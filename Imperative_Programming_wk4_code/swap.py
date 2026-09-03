"""
File:   swap.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Attempts to swap two variables
"""


def swap(argument_one, argument_two):
    temp_value = argument_one
    argument_one = argument_two
    argument_two = temp_value


a = 5
b = 6
swap(a, b)
print(a, b)
