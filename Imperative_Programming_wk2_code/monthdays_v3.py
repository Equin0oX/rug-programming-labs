"""
File:   monthdays_v3.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Returns the number of days in a month (ignoring leap days)
"""

print("Please enter a month")
month = input().lower()
match month:
    case "january" | "1" | "march" | "3" | "may" | "5" | "july" | "7" | \
            "august" | "8" | "october" | "10" | "december" | "12":
        print("That month has 31 days")
    case "april" | "4" | "june" | "6" | "september" | "9" | "november" | "11":
        print("That month has 30 days")
    case "february" | "2":
        print("That month has 28 days")
    case other:
        print("That is not a valid month.")


