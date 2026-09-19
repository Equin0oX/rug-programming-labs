"""
File:   CompleteCycle.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Reads a space-separated sequence of "next" indices from standard input
    and prints "Yes" if following them from index 0 visits every number
    exactly once and returns back to 0, otherwise prints "No".
"""

def completeCycle(path):
    numbers = [int(number) for number in path.split(" ")]
    numbers_visited = []
    lastVisitedNumber = 0
    for i in range(len(numbers)):
        numbers_visited.append(numbers[lastVisitedNumber])
        lastVisitedNumber = numbers[lastVisitedNumber]
    if sorted(numbers_visited) == sorted(numbers) and numbers_visited[-1] == 0:
        return "Yes"
    return "No"

print(completeCycle(input()))