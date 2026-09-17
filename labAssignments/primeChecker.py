"""
File:   primeChecker.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Reads an integer from standard input and prints the largest prime number
    that is less than or equal to it.
"""

def lastPrime(ceilingNumber):
    while ceilingNumber > 2:
        ceilingNumber -= 1
        if isPrime(ceilingNumber):
            return ceilingNumber
        

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


print(lastPrime(int(input())))