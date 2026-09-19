"""
File:   missingno.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Reads a space-separated sequence of numbers and prints the length of
    the longest strictly increasing run obtainable by removing at most
    one element from the sequence.
"""

def missingno(sequence):
    numbers = [int(number) for number in sequence.split(" ")]
    n = len(numbers)

    left_side = [1] * n
    for i in range(1, n):
        left_side[i] = left_side[i - 1] + 1 if numbers[i - 1] < numbers[i] else 1

    right_side = [1] * n
    for i in range(n - 2, -1, -1):
        right_side[i] = right_side[i + 1] + 1 if numbers[i] < numbers[i + 1] else 1

    answer = max(left_side)
    for i in range(1, n - 1):
        if numbers[i - 1] < numbers[i + 1]:
            answer = max(answer, left_side[i - 1] + right_side[i + 1])
    return answer

print(missingno(input()))