"""
File:   lettercount.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Prints the number of times each letter appears in a given input
"""

letter_counts = [0]*26
print("Please enter a text:")
for letter in input():
    letter_counts[ord(letter) - ord("a")] += 1

for letter in range(26):
    if letter_counts[letter] > 0:
        print(chr(ord("a") + letter) + ": " + str(letter_counts[letter]))
