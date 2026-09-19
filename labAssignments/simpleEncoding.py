"""
File:   simpleEncoding.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    This program encodes a word by shifting each letter forward in the
    alphabet by its position (index + 1), wrapping around within its case.
    Non-letter characters are left unchanged.
"""

def simple_encoder(word):
    result = ""
    for i, letter in enumerate(word):
        if 65 <= ord(letter) <= 90:
            result += chr((ord(letter) + i+1 - 65) % 26 + 65)
        elif 97 <= ord(letter) <= 122:
            result += chr((ord(letter) + i+1 - 97) % 26 + 97)
        else:
            result += letter
    return result

print(simple_encoder(input()))