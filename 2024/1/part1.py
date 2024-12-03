with open("input.txt") as f:
    left_list = sorted([int(line.split()[0]) for line in f])
    f.seek(0)
    right_list = sorted([int(line.split()[1]) for line in f])

sum_of_differences = sum([abs(j-i) for i, j in zip(left_list, right_list)])
print(sum_of_differences)