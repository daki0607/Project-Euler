"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

d = {}

def seq1(n, c, d):
    if (n == 1):
        return c
    
    n = int(n/2)
    if (n in d):
        return c + d[n]
    
    c += 1
    if (n % 2 == 0):
        return seq1(n, c, d)
    
    return seq2(n, c, d)

def seq2(n, c, d):
    if (n == 1):
        return c
    
    n = int(3*n+1)
    if (n in d):
        return c + d[n]
    
    c += 1
    return seq1(n, c, d)

for n in range(1, 1000000):
    c = 1
    if (n % 2 == 0):
        d[n] = seq1(n, c, d)
    else:
        d[n] = seq2(n, c, d)

print(max(d, key=lambda i: d[i]))
