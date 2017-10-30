"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.
"""

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
        

S = 0

for i in range(10, 100000):
    string = str(i)
    num = 0
    for j in range(len(string)):
        num += fact(int(string[j]))
    if (num == i):
        S += i

print(S)


        
