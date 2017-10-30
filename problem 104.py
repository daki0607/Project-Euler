"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F2749, which contains
575 digits, is the first Fibonacci number for which the first nine digits
are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
"""

import helper

def fib():
    """ Generates the next fibonacci number. """
    a, b = 0, 1

    while True:
        a, b = b, a+b
        yield a

def is_pandigital(n):
    num = sorted(helper.make_list(int(n)))
    test = list(range(1, 10))

    return num == test

F = fib()
f = next(F)
k = 1

while True:
    f = next(F)
    k += 1

    if (is_pandigital(str(f)[-9:]) and is_pandigital(str(f)[:9])):
        break

print(k)
