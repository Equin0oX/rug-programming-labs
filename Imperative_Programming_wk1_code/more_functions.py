"""
File:   more_functions.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    An example of functions with arguments
"""


def join_parameters(argument_one, argument_two):
    print("The value of argument_one is: " + argument_one)
    joined_arguments = argument_one + argument_two
    print("The joined argument are: " + joined_arguments)

join_parameters("hello ", "world")
