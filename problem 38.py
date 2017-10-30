"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

one_to_nine = ''.join(str(i) for i in range(1, 10))

def is_pandigital(n):
    n = str(n)
    return ''.join(sorted(n)) == one_to_nine

pandigitals = []

def calculate_pandigital_set(n):
    limit = 1

    while True:
        limit += 1
        products = [str(n*x) for x in range(1, limit+1)]
        test_number = ''.join(products)

        if (len(test_number) > 9):
            return False
        if (len(test_number) < 9):
            continue
        if (is_pandigital(test_number)):
            print(n, test_number)
            pandigitals.append(test_number)
            return True


n = 1
while (len(str(n)) < 5):
    calculate_pandigital_set(n)
    n += 1

print(max(pandigitals))


            
