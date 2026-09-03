"""
File:   lettercount_v2.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Prints the number of times each letter appears in a given input
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_counts = [0] * len(alphabet)
print("Please enter a text:")
for letter in input():
    if letter.lower() in alphabet:
        letter_counts[ord(letter.lower()) - ord("a")] += 1

for letter in range(len(alphabet)):
    if letter_counts[letter] > 0:
        print(alphabet[letter] + ": " + str(letter_counts[letter]))

