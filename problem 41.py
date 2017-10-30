"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

n = 7                      divisible by
1+2+3+4 = 10               -  
1+2+3+4+5 = 15             3 
1+2+3+4+5+6 = 21           3
1+2+3+4+5+6+7 = 28         -
1+2+3+4+5+6+7+8 = 36       3
1+2+3+4+5+6+7+8+9 = 45     3 
"""

import helper

def isPandigital(i, n):
    return sorted(helper.make_list(i)) == list(range(1, n+1))

def main(n):
    Primes = helper.primes(10**n)

    for i in range(len(Primes)-1, 0, -1):
        if (isPandigital(Primes[i], n)):
            print(Primes[i])
            break
            

if (__name__ == "__main__"):
    main(7)
    
