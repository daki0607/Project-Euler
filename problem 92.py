"""
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import collections

def sum_square(n):
    S = 0
    while (n != 0):
        S += (n % 10)**2
        n = n // 10

    return S
    #return sum([int(digit)**2 for digit in str(n)])

def find_end(n, table):
    history = []
    while (n != 1 and n != 89):
        history.append(n)
        n = sum_square(n)

    for i in history:
        table[i] = n

    return table

def main(limit):
    lookup = [None] * limit
    lookup[1] = 1
    lookup[89] = 89
    max_sum = sum_square(limit-1)

    for i in range(1, max_sum+1):
        lookup = find_end(i, lookup)

    for i in range(max_sum, limit):
        lookup[i] = lookup[sum_square(i)]

    c = collections.Counter(lookup)
    print(c[89])
    
if (__name__ == "__main__"):
    main(10000000)
