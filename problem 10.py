"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

n = 2000000
A = [True]*(n - 1)
primes = []

for i in range(2, int(math.ceil(math.sqrt(n)))):
    if (A[i - 2] == True):
        for j in range(i*i, n + 1, i):
            A[j-2] = False

for k in range(len(A)):
    if(A[k] == True):
        primes.append(k + 2)

print(sum(primes))

