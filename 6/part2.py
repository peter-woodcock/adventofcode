def parse_numeric_values(line: str) -> list:
    return int(''.join(char for char in line if char.isnumeric()))


with open("input.txt") as f:
    contents = f.read().split("\n")
    time = parse_numeric_values(contents[0])
    distance = parse_numeric_values(contents[1])

    viable_time_count = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            viable_time_count += 1

    print(viable_time_count)
