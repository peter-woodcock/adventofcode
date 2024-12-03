with open("input.txt") as f:
    total_safe = 0
    for line in f:
        report = [int(level) for level in line.split()]
        differences = [j-i for i, j in zip(report[:-1], report[1:])]

        at_least_one = all(differences)
        at_most_three = max([abs(diff) for diff in differences]) <= 3
        all_increasing = all(diff > 0 for diff in differences)
        all_decreasing = all(diff < 0 for diff in differences)

        if at_least_one and at_most_three and (all_increasing or all_decreasing):
            total_safe += 1

    print(total_safe)
