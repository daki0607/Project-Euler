"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

from helper import prime_factors

consecutive = 4
current = 1
current_consecutives = []

while (len(current_consecutives) < consecutive):
    factors = set(prime_factors(current))
    if (len(factors) == consecutive):
        current_consecutives.append(current)

    else:
        current_consecutives = []

    current += 1

print(current_consecutives)
