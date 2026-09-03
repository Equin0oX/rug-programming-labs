"""
File:   functions.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    An example of declaring and using functions
"""

def first_function():
    print("This is the start of the first function")
    second_function()
    print("This is the end of the first function")

def second_function():
    print("This is the start of the second function")
    print("This is the end of the second function")

first_function()
