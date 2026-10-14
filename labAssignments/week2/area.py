"""
File:   area.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Utility file with functions to calculate the area of a triangle and the
    area of a rectangle. Imported and tested by Themis.
"""


def get_area_of_triangle(base, height):
    return base * height / 2


def get_area_of_rectangle(length, width):
    return float(length * width)
