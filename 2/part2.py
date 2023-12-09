import re

running_total = 0


def return_highest_count_of_cube_colour(colour: str, highest_count: int) -> int:
    given_cubes = re.search(f"([0-9]+) {colour}", round)
    if given_cubes:
        return highest_count if highest_count > int(given_cubes.group(1)) else int(given_cubes.group(1))
    else:
        return highest_count


with open("test_input.txt", newline="\n") as f:
    for line in f:
        highest_red = 0
        highest_blue = 0
        highest_green = 0

        rounds = line[8:].split(";")
        for round in rounds:
            highest_red = return_highest_count_of_cube_colour("red", highest_red)
            highest_blue = return_highest_count_of_cube_colour("blue", highest_blue)
            highest_green = return_highest_count_of_cube_colour("green", highest_green)

        running_total += highest_red * highest_blue * highest_green

print(running_total)