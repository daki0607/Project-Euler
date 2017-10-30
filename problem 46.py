"""
It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from helper import lookup_primes

limit = 10000

def is_int(n):
    return n == int(n)

primes = lookup_primes(limit)

def is_goldbach(n):
    for i in range(5, n, 2):
        if (primes[i]):
            result = ((n-i) / 2) ** 0.5
            if (is_int(result)):
                return True

    return False


# print(is_goldbach(9))
# print(is_goldbach(15))

ind = 5
while True:
    if (not primes[ind]):
        if (not is_goldbach(ind)):
            print(ind)
            break

    ind += 2
        




    

