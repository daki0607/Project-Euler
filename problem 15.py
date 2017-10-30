"""
How many such routes are there through a 20×20 grid?
"""

import math

l, w = 20, 20
total = l + w
print(int(math.factorial(total) / math.factorial(l) / math.factorial(w)))
