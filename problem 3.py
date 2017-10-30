"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = int(input("number = "))

def primes(x):
    i = 1
    factors = []
    while (i < x / 2):
        if (x % i == 0):
            x = x / i
            factors.append(i)
        i += 1
    factors.append(x)

    return factors

print(primes(number))
        
        
