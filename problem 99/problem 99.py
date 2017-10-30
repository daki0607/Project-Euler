"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more
difficult, as both numbers contain over three million digits.

Determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

import helper as hl

f = open("p099_base_exp.txt").read()
f = f.split("\n")
f = [i.split(",") for i in f]
f = [[int(i[0]), int(i[1])] for i in f]

highest = (0, 0)

for ind, i in enumerate(f):
    if (hl.power(i[0], i[1]) > highest[1]):
        highest = (ind, hl.power(i[0], i[1]))

print(highest[0])
