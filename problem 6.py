"""
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
"""
number_set = []
for i in range(1, 101):
    number_set.append(i)

sum_square = 0
square_sum = 0

def sum_num(n):
    x = 0
    for i in range(len(n)):
        x += n[i] ** 2

    return x

def square(n):
    x = 0
    for i in range(len(n)):
        x += n[i]

    return x ** 2

print(square(number_set) - sum_num(number_set))
"""

print(sum(range(1,101))**2 - sum(map(lambda x: x**2, range(1,101))))
