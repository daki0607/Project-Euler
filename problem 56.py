"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the 
maximum digital sum?
"""

limit = 100

def digit_sum(n):
    return sum(int(l) for l in str(n))

"""
max_sum = 0
limit = 100

for a in range(0, limit+1):
    for b in range(0, limit+1):
        P = digit_sum(a**b)
        if (P > max_sum):
            max_sum = P

print(max_sum)
return None
"""

max_sum = max(digit_sum(a**b) for a in range(0, limit+1) for b in range(0, limit+1))

print(max_sum)
