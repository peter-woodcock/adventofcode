def parse_numeric_values(line: str) -> list:
    return ''.join([value for value in line.split() if value.isnumeric()])


with open("input.txt") as f:
    contents = f.read().split("\n")
    time = int(parse_numeric_values(contents[0]))
    distance = int(parse_numeric_values(contents[1]))

    viable_time_count = 0
    for i in range(1, int(parse_numeric_values(contents[0]))):
        if i * (int(time) - i) > distance:
            viable_time_count += 1

    print(viable_time_count)
