"""
File:   hitDetection.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    This program takes inputs for coordinates of opposing corners of a rectangle, and a point on the field, then prints out where the point lies in relation to the shape.
"""

corner1 = (int(input()),int(input()))
corner2 = (int(input()),int(input()))
point = (int(input()),int(input()))

if min(corner1[0], corner2[0]) < point[0] < max(corner1[0], corner2[0]) and min(corner1[1], corner2[1]) < point[1] < max(corner1[1], corner2[1]):
    print("INSIDE")
elif min(corner1[0], corner2[0]) <= point[0] <= max(corner1[0], corner2[0]) and min(corner1[1], corner2[1]) <= point[1] <= max(corner1[1], corner2[1]):
    print("EDGE")
else :
    print("OUTSIDE")