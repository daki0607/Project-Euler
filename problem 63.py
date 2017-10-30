"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit 
number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def digit_num(power):
    """ Returns number of power-length numbers. """
    count = 0
    i = 1
    while True:
        num_len = len(str(i**power))
        if (num_len > power):
            return count
        if (num_len== power):
            count += 1
        
        i += 1

print(sum([digit_num(x) for x in range(1, 25)]))
