"""
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

import helper as hp

i = 3

while True:
    #Generate triangle numbers
    tri_num = int((i + 1) * (i / 2))

    if (i % 2 == 0):
        num_fac = len(hp.divisors(int(i/2))) * len(hp.divisors(int(i+1)))
    else:
        num_fac = len(hp.divisors(i)) * len(hp.divisors(int((i+1) / 2)))
    if (num_fac > 500):
        break
    i += 1

print(tri_num, num_fac)
