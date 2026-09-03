"""
File:   monthdays_v2.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Returns the number of days in a month (ignoring leap days)
"""

print("Please enter a month")
month = input().lower()
if month == "january" or month == "1":
    print("That month has 31 days")
elif month == "february" or month == "2":
    print("That month has 28 days")
elif month == "march" or month == "3":
    print("That month has 31 days")
elif month == "april" or month == "4":
    print("That month has 30 days")
elif month == "may" or month == "5":
    print("That month has 31 days")
elif month == "june" or month == "6":
    print("That month has 30 days")
elif month == "july" or month == "7":
    print("That month has 31 days")
elif month == "august" or month == "8":
    print("That month has 31 days")
elif month == "september" or month == "9":
    print("That month has 30 days")
elif month == "october" or month == "10":
    print("That month has 31 days")
elif month == "november" or month == "11":
    print("That month has 30 days")
elif month == "december" or month == "12":
    print("That month has 31 days")
else:
    print("That is not a valid month.")
