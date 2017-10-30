"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

def cancel(a, b):
    ans = a/b
    a, b = str(a), str(b)
    for i in a:
        if (i in b):
            newa = int(a.replace(i, ""))
            newb = int(b.replace(i, ""))
            if (newa/newb == ans):
                return True

    return False

fractions = []

for i in range(12, 100):
    for j in range(12, i):
        if ((i % 10 == 0 or j % 10 == 0) or (i % 11 == 0 or j % 11 == 0) or i == j):
            pass
        else:
            if (cancel(j, i)):
                fractions.append((j, i))

print(fractions)
