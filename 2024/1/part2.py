from collections import Counter

with open("input.txt") as f:
    left_list = sorted([int(line.split()[0]) for line in f])
    f.seek(0)
    right_list = sorted([int(line.split()[1]) for line in f])

similarity_score = sum([x * Counter(right_list)[x] for x in left_list])
print(similarity_score)