def dampener(report: list) -> list:
    dampened_lists = []
    for idx, level in enumerate(report):
        dampened_lists += [report[:idx] + report[idx+1:]]
    return dampened_lists


def is_safe(report: str) -> bool:
    differences = [j - i for i, j in zip(report[:-1], report[1:])]

    at_least_one = all(differences)
    at_most_three = max([abs(diff) for diff in differences]) <= 3
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    return at_least_one and at_most_three and (all_increasing or all_decreasing)


with open("input.txt") as f:
    total_safe = 0
    not_safe = []
    for line in f:
        report = [int(level) for level in line.split()]
        if is_safe(report):
            total_safe += 1
        else:
            not_safe += [report]

    for report in not_safe:
        for dampened_report in dampener(report):
            if is_safe(dampened_report):
                total_safe += 1
                break

    print(total_safe)
