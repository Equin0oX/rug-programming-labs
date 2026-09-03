"""
File:   istest.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    A test on the limits of the is operator
"""


print("Primitive types")
a = True
b = 1
print(a, "==", b, "->", a == b)
print(a, "is", b, "->", a is b)

a = 1.0
b = 1
print(a, "==", b, "->", a == b)
print(a, "is", b, "->", a is b)

print("Lists")
a = [1,2,3]
b = [1,2,3]
print(a, "==", b, "->", a == b)
print(a, "is", b, "->", a is b)
b = a
print(a, "==", b, "->", a == b)
print(a, "is", b, "->", a is b)

print("Strings")
a = "test"
b = "test"
print(a, "==", b, "->", a == b)
print(a, "is", b, "->", a is b)
b = "tes"
b += "t"
print(a, "==", b, "->", a == b)
print(a, "is", b, "->", a is b)
print("35" is str(35))
