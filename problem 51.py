"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.
"""

from helper import lookup_primes
from itertools import permutations

P = lookup_primes(1000000)

def prime_family(n):
    """ Permutes all *s in n and returns the number of primes. """
    family = []
    for i in range(1, 10):
        n_ = int(n.replace("*", str(i)))
        if (P[n_]):
            family.append(n_)

    l = len(family)
    if (l == 8):
        print(min(family), n)
    return l

g = [list(permutations(["*", "*", "*", str(x), str(y), str(z)])) for x in range(1, 10) for y in range(1, 10) for z in range(1, 10)]
g = [i for sub in g for i in sub]
g = list(map(lambda l: "".join(str(i) for i in l), g))

for _ in g:
    prime_family(_)
