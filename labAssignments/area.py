"""
File:   helloworld.py
Author: Sebastian Ševčík (s.sevcik@student,rug.nl)

Description:
    This program takes input of a shape and two sides, then prints the size of the area of the shape to the console.
"""

def get_area_of_triangle(base, height):
    return (base * height) / 2

def get_area_of_rectangle(length, width):
    return length * width

shape = input().lower()
sideA = float(input())
sideB = float(input())

if shape == "triangle":
    print(get_area_of_triangle(sideA, sideB))
else:
    print(get_area_of_rectangle(sideA, sideB))