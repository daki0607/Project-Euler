"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = []
num = 2

while len(primes) < 10001:
    if (num > 1):
        for i in range(2, num):
            if (num % i == 0):
                num += 1
                break
        else:
            primes.append(num)
            num += 1
    

print(primes[-1])
