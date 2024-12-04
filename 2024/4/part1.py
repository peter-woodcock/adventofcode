from collections import defaultdict


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))


def count_of_xmas(test_list) -> int:
    forwards = sum(1 for i in range(len(test_list)) if test_list[i:i+len(['X', 'M', 'A', 'S'])] == ['X', 'M', 'A', 'S'])
    backwards = sum(1 for i in range(len(test_list)) if test_list[i:i + len(['S', 'A', 'M', 'X'])] == ['S', 'A', 'M', 'X'])
    return forwards + backwards


with open('input.txt') as f:
    lines = [[chr for chr in line] for line in f.read().splitlines()]

cols = groups(lines, lambda x, y: x)
rows = groups(lines, lambda x, y: y)
fdiag = groups(lines, lambda x, y: x + y)
bdiag = groups(lines, lambda x, y: x - y)


total = 0
for search_path in cols + rows + fdiag + bdiag:
    total += count_of_xmas(search_path)

print(total)