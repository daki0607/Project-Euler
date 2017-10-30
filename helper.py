#A bunch of helper functions
from random import randrange

def primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * int(((n - i * i - 1)/(2 * i) + 1))

    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def lookup_primes(limit):
    """ Returns a lookup table of primes < n """
    is_prime = [False] * 2 + [True] * (limit - 1)
    
    for n in range(int(limit**0.5 + 1.5)): # stop at sqrt(limit)
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
                
    return is_prime

def array_split(array, width):
    """ Splits an array into sub-arrays of size 'width'. """
    arrays = []
    
    while (len(array) > width):
        piece = array[:width]
        arrays.append(piece)
        array = array[width:]
        
    arrays.append(array)

    return arrays

def factorize(n):
    """ Returns the prime factorization of a number. """
    primenums = primes(n)
    factors = []
    
    for p in primenums:
        if (p*p > n):
            break
        i = 0
        
        while (n % p == 0):
            n //= p
            i += 1
            
        if (i > 0):
            factors.append((p, i))
            
    if (n > 1):
        factors.append((n, 1))

    return factors

def factors(n):
    """ Returns the factors of a number. """
    if (n > 0):
        factors = factorize(n)
        div = [1]
        
        for (p, r) in factors:
            div = [d * p**e for d in div for e in range(r + 1)]
            
        return sorted(div)
    
    else:
        return [0]

def isPrime(n, k=10):
    """ Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite. """

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                    367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
                    433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
                    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571]
    
    if (n < 2):
        return False
    
    for p in small_primes:
        if (n < p * p):
            return True
        if (n % p == 0):
            return False
        
    r, s = 0, n - 1
    
    while (s % 2 == 0):
        r += 1
        s //= 2
        
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        
        if (x == 1 or x == n - 1):
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            
            if (x == n - 1):
                break
            
        else:
            return False
        
    return True

def fib(n):
    """ Returns the nth term in the Fibonacci Sequence. """
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a+b
        
    return a

def fiblist(n):
    """ Returns a list of Fibonacci Numbers < n """
    a, b = 0, 1
    F = []
    
    while b < n:
        a, b = b, a+b
        F.append(a)

    return F

def power(x, n):
    """ Returns x^n """
    y = 1

    while True:
        t = n % 2
        n = n // 2

        if (t == 1):
            y *= x
            
        if (n == 0):
            break
        
        x *= x
        
    return y

def make_int(n):
    """ Turns iterable into an integer """
    return int(''.join(map(str, n)))

def make_list(n):
    """ Turns an integer into a list """
    return list(map(int, str(n)))

def is_palindrome(s):
    """ Determines if a string is a palindrome. """
    return s == s[::-1]

def sub_palindrome(s, n):
    """ Finds number of palindromes of size n contained within s. """
    count = 0
    for i in range(len(s)-n+1):
        if (pal(s[i:i+n])):
            count += 1

    return count

def prime_factors(n):
    factors = []
    while (n % 2 == 0):
        factors.append(2)
        n /= 2
    n = int(n)
    P = primes(n+1)
    for p in P:
        if (n % p == 0):
            factors.append(p)
    return factors
