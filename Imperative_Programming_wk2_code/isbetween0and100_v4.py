"""
File:   isbetween0and100_v4.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Determines whether an entered number is between 0 and 100
"""

print("Please enter a number")
number = int(input())
if 0 < number < 100:
    print("That number is between 0 and 100")
else:
    if number <= 0:
        print("That number is not positive")
    else:
        print("That number is at least 100")
