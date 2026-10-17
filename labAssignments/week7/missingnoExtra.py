"""
File:   missingnoExtra.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Reads a space-separated sequence of numbers and a maximum k. Prints the
    length of the longest strictly increasing run obtainable by removing at
    most k elements from the sequence.
"""

def missingno_extra(numbers, max_removals):
    amount_of_numbers = len(numbers)
    table = []
    for i in range(amount_of_numbers):
        row = []
        for i in range(max_removals + 1):
            row.append(1)
        table.append(row)

    for i in range(amount_of_numbers):
        earliest_prev = max(0, i - 1 - max_removals)
        for prev in range(earliest_prev, i):
            if numbers[prev] < numbers[i]:
                skipped = i - prev - 1
                for budget in range(skipped, max_removals + 1):
                    longer_run = table[prev][budget - skipped] + 1
                    if longer_run > table[i][budget]:
                        table[i][budget] = longer_run

    best = 0
    for i in range(amount_of_numbers):
        if table[i][max_removals] > best:
            best = table[i][max_removals]
    return best


def main():
    numbers = [int(number) for number in input().split()]
    max_removals = int(input())
    print(missingno_extra(numbers, max_removals))


main()
