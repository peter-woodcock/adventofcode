def parse_numeric_values(line: str) -> list:
    return [int(value) for value in line.split() if value.isnumeric()]


with open("input.txt") as f:
    contents = f.read().split("\n")
    times_and_distances = {key: value for key, value
                           in zip(parse_numeric_values(contents[0]), parse_numeric_values(contents[1]))}

    running_total = 1
    for time in times_and_distances:
        viable_time_count = 0
        for i in range(1, int(time)):
            if i * (int(time) - i) > times_and_distances[time]:
                viable_time_count += 1
        running_total *= viable_time_count

    print(running_total)
