"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than
28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which !!cannot!! be written as the sum
of two abundant numbers.
"""

"""
Go through numbers to 28123 (i)
  Generate list of abundant numbers (sum of perfect divisors is greater than n)
  For each value less than i
    Subtract value from i and check if it is list of abundant numbers
    If not, add it to the total
"""

import helper as hl

def abundant(n):
  p = hl.primes(n)
  ab = []
  for i in range(n):
    if (i in p):
      pass
    s = sum(hl.factors(i)[:-1])
    if (s > i):
      ab.append(i)

  return ab

n = 28123
abun = abundant(n)
nums = [False] * n # True means it is the sum of 2
total = 0

for i in range(len(abun)):
  for j in range(i, len(abun)):
    # If the result is less than n, it is the sum of 2 abundant numbers
    if (abun[i] + abun[j] < n):
      nums[abun[i] + abun[j]] = True

for i in range(len(nums)):
  if (not nums[i]):
    total += i

print(total)
