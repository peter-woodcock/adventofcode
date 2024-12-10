NEXT_DIRECTION = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

def get_starting_coordinates(lines):
    for y, line in enumerate(lines):
        try:
            x = line.index('^')
        except ValueError:
            continue
        if x:
            return [x, y]


def get_next_coordinate(current_coordinates, direction):
    x, y = current_coordinates
    direction_to_coordinate_change = {
        "N": [x, y - 1],
        "E": [x + 1, y],
        "S": [x, y + 1],
        "W": [x - 1, y],
    }
    return direction_to_coordinate_change[direction]


with open('input.txt') as f:
    lines = [[chr for chr in line] for line in f.read().splitlines()]

current_coordinates = get_starting_coordinates(lines)
direction = "N"

while True:
    next_coordinates = get_next_coordinate(current_coordinates, direction)
    if any(e in next_coordinates for e in [-1, len(lines)]):
        lines[current_coordinates[1]][current_coordinates[0]] = 'X'
        break
    if lines[next_coordinates[1]][next_coordinates[0]] == '#':
        direction = NEXT_DIRECTION[direction]
    else:
        lines[current_coordinates[1]][current_coordinates[0]] = 'X'
        current_coordinates = next_coordinates

unique_positions = 0
for line in lines:
    unique_positions += line.count('X')

print(unique_positions)