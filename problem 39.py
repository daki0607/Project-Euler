"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def max_ind(li):
    """ Returns the index of the largest element. """
    maximum = 0
    index = 0
    for ind, i in enumerate(li):
        if (i > maximum):
            maximum = i
            index = ind

    return index

def main():
    num_solutions = [0]*1001
    for p in range(1000, 120, -2):
        count = 0

        for c in range(int(p/2), 0, -1):
            for b in range(c, 0, -1):
                a = (c**2 - b**2)**0.5
                if (a+b+c == p):
                    count += 1
                    break
        
        num_solutions[p] = count

    print(max_ind(num_solutions))
                
if (__name__ == "__main__"):
    main()
