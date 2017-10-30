"""
Find the minimal path sum, in matrix.txt from the top left to the bottom right
by only moving right and down.
"""

with open("p081_matrix.txt", "r") as file:
    matrix = file.readlines()

for index, line in enumerate(matrix):
    matrix[index] = line.rstrip().split(",")
    matrix[index] = list(map(int, matrix[index]))

S = 0

    
