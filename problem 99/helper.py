#A bunch of helper functions

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * int(((n - i * i - 1)/(2 * i) + 1))

    return [2] + [i for i in range(3, n, 2) if sieve[i]]

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

def isprime(n):
    """ Checks if a number is prime """
    return (len(factors(n)) <= 2)

def fib(n):
    """ Returns the nth term in the Fibonacci Sequence. """
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a+b
        
    return a

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

