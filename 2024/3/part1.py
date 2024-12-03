import re

pattern = re.compile('mul\((\d*),(\d*)\)')

with open("input.txt") as f:
    memory = f.read()

multipliers = (pattern.findall(memory))
print(sum([int(i) * int(j) for i, j in multipliers]))
