"""
File:   isbetween0and100.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Determines whether an entered number is between 0 and 100
"""

print("Please enter a number")
number = int(input())
if number > 0:
    if number < 100:
        print("That number is between 0 and 100")
