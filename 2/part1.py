import re

maximum_number_of_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def given_cubes_greater_than_possible(colour: str):
    given_cubes = re.search(f"([0-9]+) {colour}", round)
    if given_cubes:
        return int(given_cubes.group(1)) > maximum_number_of_cubes[colour]


running_total = 0

with open("input.txt", newline="\n") as f:
    for line in f:
        game_possible = True
        game_id = int(re.search("([0-9]+):", line).group(1))

        rounds = line[8:].split(";")
        for round in rounds:
            for colour in maximum_number_of_cubes.keys():
                if given_cubes_greater_than_possible(colour):
                    game_possible = False
                    break

        if game_possible:
            running_total += game_id

print(running_total)
