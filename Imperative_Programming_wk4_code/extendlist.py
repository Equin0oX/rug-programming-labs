"""
File:   extendlist.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    Attempts to double a list using the method extend
"""


def double_list(lst_arg):
    lst_arg.extend(lst_arg)


lst = [5, 6]
double_list(lst)
print(lst)
