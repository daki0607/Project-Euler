"""
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

highest = 0

def palindrome(n):
    n = str(n)
    return n == n[::-1]


for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if palindrome(i * j):
            #print(i * j)
            if (i * j > highest):
                highest = i * j

print(highest)
            
                

