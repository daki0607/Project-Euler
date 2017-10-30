"""
Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤ n ≤ 39. However, when n=40,40^2+40+41=40(40+1)+41
is divisible by 41, and certainly
when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces
80 primes for the consecutive values 0 ≤ n ≤ 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of nn
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""

import helper

def quadratic(a, b):
    """ Returns the number of consecutive primes produced with a and b """
    n = 0
    while (helper.isprime(abs(n**2 + a*n + b))):
        n += 1

    return n

x = helper.primes(1000)
y = helper.primes(1000)

for i in range(len(y)):
    y[i] *= -1

a = x + y
b = x + y
maxPrimes = 0
coefficients = [0, 0]

for i in range(len(a)):
    for j in range(len(b)):
        if (quadratic(a[i], b[j]) > maxPrimes):
            maxPrimes = quadratic(a[i], b[j])
            coefficients = [a[i], b[j]]

print(maxPrimes, coefficients, coefficients[0] * coefficients[1])
