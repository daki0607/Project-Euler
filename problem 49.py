"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import helper

def check(a, b):
    # Checks if 2 numbers a permutations of one another
    a = sorted(helper.make_list(a))
    b = sorted(helper.make_list(b))

    for i in range(len(a)):
        if (a[i] != b[i]):
            return False

    return True
    

def main():
    P = helper.primes(10000) # Starts at 0, ends at 10000

    for i in range(len(P)):
        for j in range(i+1, len(P)):
            # P[j] > P[i]
            k = (P[j]-P[i]) + P[j]
            if (k in P):
                if (check(P[i], P[j]) and check(P[j], k)):
                    S = str(P[i]) + str(P[j]) + str(k)
                    if (len(S) == 12):
                        print(S)
                        break

if (__name__ == "__main__"):
    main()
    
