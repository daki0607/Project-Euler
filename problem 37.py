"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import helper

def trun_L(n):
    n = str(n)
    for i in range(len(n)):
        yield n[i:]

def trun_R(n):
    n = str(n)
    for i in range(len(n)):
        if (i == 0):
            yield n[:]
        else:
            yield n[:-i]

P = helper.primes(10000)
exceptions = [2, 3, 5, 7]
truncatable = []
trun = []

for i in P:
    L = trun_L(i)
    R = trun_R(i)

    for j in range(len(str(i))):
        l = int(next(L))
        r = int(next(R))
        if ((l not in P) and (r not in P)):
            break

    else:
        truncatable.append(i)

for a in range(len(truncatable)):
    if (truncatable[a] not in exceptions):
        trun.append(truncatable[a])

print(truncatable)
