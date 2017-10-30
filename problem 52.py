"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

# 999999 / 6 = 166666.5 => 166666
# Therefore, x <= 166666

import helper

def same_digits(li):
    """ Checks if all elements in the list use the same digits. """
    li = list(map(helper.make_list, li))
    li = list(map(sorted, li))
    
    for i in range(len(li[0])):
        for j in range(1, len(li)):
            if (li[0][i] != li[j][i]):
                return False

    return True

def main():
    for x in range(10000, 166666):
        numbers = [x*a for a in [1, 2, 3, 4, 5, 6]]
        if (same_digits(numbers)):
            print(x)

if (__name__ == "__main__"):
    main()
