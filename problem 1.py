"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
"""
def multiples(n):
    sum = 0
    i = 1
    while (i < n):
        if (i % 3 == 0):
            sum += i
            i += 1
        elif (i % 5 == 0):
            sum += i
            i += 1
        else:
            i += 1

    return sum

x = int(input("n = "))
print(multiples(x))
"""

print(sum(range(3, 1000, 3)) + sum(range(5, 1000, 5)) - sum(range(15, 1000, 15)))
