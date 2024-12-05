with open('input.txt') as f:
    lines = [[chr for chr in line] for line in f.read().splitlines()]

total = 0

valid_xs = [
    ['M', 'M', 'S', 'S'],
    ['M', 'S', 'M', 'S'],
    ['S', 'S', 'M', 'M'],
    ['S', 'M', 'S', 'M']
            ]

for i, line in enumerate(lines):
    if i == 0 or i == len(lines) - 1:
        continue
    for j, chr in enumerate(line):
        if j == 0 or j == len(line) - 1:
            continue
        if chr == 'A':
            for valid_x in valid_xs:
                if lines[i-1][j-1] == valid_x[0] and lines[i-1][j+1] == valid_x[1] and lines[i+1][j-1] == valid_x[2] and lines[i+1][j+1] == valid_x[3]:
                    total += 1

print(total)