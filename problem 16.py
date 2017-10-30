"""
What is the sum of the digits of the number 2^1000?
"""

n = 0
for i in str(2**1000):
    n += int(i)

print(n)
