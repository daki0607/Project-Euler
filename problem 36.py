"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from helper import pal

# Base 10 to base 2
# str(bin(i))[2:]

S = 0

for i in range(1, 1000000, 2):
    if (pal(str(i))):
        if (pal(str(bin(i))[2:])):
            S += i 

print(S)
