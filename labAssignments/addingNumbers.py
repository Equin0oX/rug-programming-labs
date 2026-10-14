"""
File:   addingNumbers.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Reads three integers n, m, k from standard input and prints the sum of
    the numbers from n to m (inclusive) in steps of size k.
"""

def numAdder(start, end, step):
    start = int(start)
    end = int(end)
    step = int(step)
    end = end - ((end - start)%step)
    result = (start + end)*(end - start + step)//(2*step)
    return result

print(numAdder(*input().split(" ")))
