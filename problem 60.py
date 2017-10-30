"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
these four primes, 792, represents the lowest sum for a set of four primes
with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from helper import primes
from helper import isPrime
from time import time

s = time()
limit = 5000
P = primes(limit)

concatable = []
for i in range(len(P)):
    current = []
    
    for j in range(1, len(P)):
        conc = int("".join([str(P[i]), str(P[j])]))
        
        if (isPrime(conc)):
            current.append(P[j])
            
    concatable.append(current)

print(time()-s)

