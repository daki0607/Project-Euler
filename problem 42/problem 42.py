"""
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call
the word a triangle word.

Using words.txt, a 16K text file
containing nearly two-thousand common English words,
how many are triangle words?
"""

import math

#Up to 23rd term (10 z's)

def triangle(n):
    """ Returns a list of triangle numbers up to the nth term. """
    return list(map(lambda x: int(0.5*x * (x+1)), range(1, n+1)))

seq = triangle(23)
values = dict([(chr(x), x - 96) for x in range(97, 123)])
triWords = 0

# Parse the file
f = open("p042_words.txt")
f = f.read()
f = list(f.split(","))
for i in range(len(f)):
    f[i] = f[i].lower()

for i in f:
    score = 0
    for j in i:
        score += values[j]
    if (score in seq):
        triWords += 1

print(triWords)
        
