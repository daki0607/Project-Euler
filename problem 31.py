"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

"""
coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200

table = {}
for y in range(0, target + 1):
    table[y, 0] = 1

for y in range(0, target + 1):
    for x in range(1, len(coins)):
        table[y, x] = 0
        if (y >= coins[x]):
            table[y, x] += table[y, x - 1]
            table[y, x] += table[y - coins[x], x]

        else:
            table[y, x] = table[y, x - 1]

print(table[200, x])
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
ways = [0] * (amount + 1)
ways[0] = 1

for i in range(8):
    for j in range(coins[i], amount + 1):
        ways[j] = ways[j] + ways[j - coins[i]]

print(ways[amount])




