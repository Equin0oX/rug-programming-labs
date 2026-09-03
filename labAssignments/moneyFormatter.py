"""
File:   helloworld.py
Author: Sebastian Ševčík (s.sevcik@student,rug.nl)

Description:
    This program takes a decimal value and splits it into euros and cents, then prints to the console.
"""

def money_formatter(amount):
    euros = int(amount)
    cents = round((amount - euros) * 100)
    return f"{euros} euro {cents}"

print(money_formatter(float(input())))