"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

1, 2, 3, 2^2, 5, 2^1*3^1, 7, 2^3, 3^2, 2^1*5^1 - 10

5, 7, 2^3, 3^2 - for 10

11, 12, 13, 14, 15, 16, 17, 18, 19, 20
11, 2^2 3^1, 13, 2^1 7^1, 3^1 5^1, 2^4, 17, 2^1 3^2, 19, 2^2 5^1 - 11 to 20

5, 7, 2^4, 3^2, 11, 13, 17, 19 - 1 to 20
"""
print(5*7*16*9*11*13*17*19)


