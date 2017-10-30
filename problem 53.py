"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!/r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are 
greater than one-million?
"""

"""
If aCr > 1000000, then for all n > a, nCr > 1000000

100C4 > 1000000, therefore 100C96 > 1000000

Have to find the n value for an r which nCr exceeds one-million.
"""

from math import factorial

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def main():
    r_vals = [0]*100
    for r in range(4, 97):
        n = r+1
        while (choose(n, r) < 1000000):
            n += 1
        
        r_vals[r] = n

    r_vals = r_vals[4:97]

    total = 0
    for i in r_vals:
        total = total + (100 - i) + 1
    
    return total

print(main())
