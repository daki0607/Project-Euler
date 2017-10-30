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


limit = 1000000 # Search under 1 million
factors = [0]*limit # Number of prime factors
count = 0

for i in range(2, limit):
    if (factors[i] == 0):
        # i is prime
        count = 0
        val = i

        while (val < limit):
            # add 1 prime factor every i'th number
            factors[val] += 1
            val += i

    elif (factors[i] == 4):
        count += 1
        if (count == 4):
            print(i-3) # The first number
            break

    else:
        count = 0
