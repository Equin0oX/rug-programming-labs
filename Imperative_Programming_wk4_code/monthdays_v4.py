"""
File:   monthdays_v4.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Returns the number of days in a month (ignoring leap days)
"""

print("Please enter a month")
month = input().lower()
if month in ["january", "1", "march", "3", "may", "5", "july", "7", "august", "8", "october", "10", "december", "12"]:
    print("That month has 31 days")
elif month in ["april", "4", "june", "6", "september", "9", "november", "11"]:
    print("That month has 30 days")
elif month in ["february", "2"]:
    print("That month has 28 days")
else:
    print("That is not a valid month.")
