"""
File:   numbers.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    A showcase of differences between ints and floats
"""

print(123456789   * 123456789)           # 15241578750190521
print(123456789.0 * 123456789)           # 1.524157875019052e+16
print(float(42))                         # 42.0
print(int(42.0))                         # 42
print(int(123456789.0 * 123456789))      # 15241578750190520
print(int(123456789.0) * 123456789)      # 15241578750190521
