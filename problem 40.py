"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def champ():
    i = 1
    while True:
        yield str(i)
        i += 1

indexes = list(map(lambda x: 10 ** x, range(7)))
digits = []
pos = 0
C = champ()
c = next(C)
value = 1

while len(digits) != len(indexes):
    for i in range(len(c)):
        pos += 1
        if (pos in indexes):
            digits.append(c[i])

    c = next(C)

for j in digits:
    value *= int(j)

print(value)
