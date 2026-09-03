"""
File:   swap_list.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Attempts to swap two entries in a list
"""


def swap(lst_arg):
    temp_value = lst_arg[0]
    lst_arg[0] = lst_arg[1]
    lst_arg[1] = temp_value


lst = [5, 6]
swap(lst)
print(lst)
