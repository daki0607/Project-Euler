"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import helper

def isRotatable(n, primes):
    n = str(n)
    for i in range(len(n)):
        rotn = n[i:] + n[:i]
        if (not primes[int(rotn)]):
            return False

    return True

primes = helper.lookup_primes(1000000)
circular = 2

for prime, isPrime in enumerate(primes):
    if ((not isPrime)         or ("2" in str(prime)) or 
        ("4" in str(prime)) or ("6" in str(prime)) or 
        ("8" in str(prime)) or ("0" in str(prime)) or 
        ("5" in str(prime))):
        continue
    
    if (isRotatable(prime, primes)):
        circular += 1
    
print(circular)

            
        
    

    
