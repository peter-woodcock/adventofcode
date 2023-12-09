import re

maximum_number_of_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def given_cubes_greater_than_possible(colour: str, round) -> bool:
    given_cubes = re.search(f"([0-9]+) {colour}", round)
    return int(given_cubes.group(1)) > maximum_number_of_cubes[colour] if given_cubes else False


running_total = 0

with open("input.txt", newline="\n") as f:
    for line in f:
        game = line[8:].split(";")
        game_possible = all(
            all(not given_cubes_greater_than_possible(colour, round) for colour in maximum_number_of_cubes)
            for round in game
        )

        if game_possible:
            game_id = int(re.search("([0-9]+):", line).group(1))
            running_total += game_id


print(running_total)
