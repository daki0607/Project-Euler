"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

import helper

P = helper.primes(1000000)
primes = []

def add_prime():
    S = 0
    i = 12
    while True:
        S += P[i]
        i += 1
        yield S

pAdd = add_prime()
p = next(pAdd)

while True:
    if (p > P[-1]):
        break

    if (p in P):
        primes.append(p)

    p = next(pAdd)

print(primes[-1])
