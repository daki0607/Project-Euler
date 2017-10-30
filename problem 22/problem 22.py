"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

codes = []
for i in range(26):
  codes.append(chr(97 + i))
  codes.append(i + 1)

i = iter(codes)
letters = dict(zip(i, i))
  
file = open("p22_names.txt")
file = file.read()
file = file.split(",")
for i in range(len(file)):
  file[i] = file[i].lower()

file = sorted(file)
scores = [0] * len(file)
for i in range(len(file)):
  for j in range(len(file[i])):
    scores[i] += letters[file[i][j]]

total = 0
for i in range(len(scores)):
  total += scores[i] * (i + 1)

print(total)
