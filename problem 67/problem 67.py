"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt,
a 15K text file containing a triangle with one-hundred rows.
"""


def addRows(arr, i):
    """ Adds the current row to the next row. """
    for a in range(len(arr[i+1])):
        arr[i+1][a] += max(arr[i][a], arr[i][a+1])

    return arr


f = open("p067_triangle.txt")
f = f.read()
f = f.split("\n")

for i in range(len(f)):
    f[i] = f[i].split(" ")

f.pop()

for i in range(len(f)):
    for j in range(len(f[i])):
        f[i][j] = int(f[i][j])

f = f[::-1]

for i in range(len(f)-1):
    addRows(f, i)

print(f[-1])
