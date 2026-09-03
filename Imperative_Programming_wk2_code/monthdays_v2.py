"""
File:   monthdays_v2.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Returns the number of days in a month (ignoring leap days)
"""

print("Please enter a month")
month = input().lower()
if month == "february" or month == "2":
    print("That month has 28 days")
elif month == "january" or month == "1" or month == "march" or month == "3" or \
        month == "may" or month == "5" or month == "july" or month == "7" or \
        month == "august" or month == "8" or month == "october" or month == "10" or \
        month == "december" or month == "12":
    print("That month has 31 days")
elif month == "april" or month == "4" or month == "june" or month == "6" or \
        month == "september" or month == "9" or month == "november" or month == "11":
    print("That month has 30 days")
else:
    print("That is not a valid month.")
