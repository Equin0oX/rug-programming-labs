"""
File:   columnar.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Encrypts text using a columnar transposition cipher: characters are
    distributed round-robin into num_of_columns columns, then the columns
    are read back out in the order given by the digits of encoding
    (ascending) and joined with no separators.
"""

def columnar(text, encoding):
    letter_table = []
    num_of_columns = len(str(encoding))
    for i in range(num_of_columns):
        letter_table.append([])
    for i, letter in enumerate(text):
        letter_table[i%num_of_columns].append(letter)
    pairs = []
    for i in range(num_of_columns):
        pairs.append((encoding[i], i))
    pairs.sort()
    order = [i for digit, i in pairs]

    result = ""
    for i in range(num_of_columns):
        result += "".join(letter_table[order[i]])

    return result


print(columnar(input(), input()))