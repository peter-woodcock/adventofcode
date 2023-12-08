import re

number_of_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

running_total = 0

with open("input.txt", newline="\n") as f:
    for line in f:
        game_possible = True
        game_id = int(re.search("([0-9]+):", line).group(1))

        rounds = line[8:].split(";")
        for round in rounds:
            blue_cubes = re.search("([0-9]+) blue", round)
            if blue_cubes:
                if int(blue_cubes.group(1)) > number_of_cubes["blue"]:
                    game_possible = False
                    break

            red_cubes = re.search("([0-9]+) red", round)
            if red_cubes:
                if int(red_cubes.group(1)) > number_of_cubes["red"]:
                    game_possible = False
                    break

            green_cubes = re.search("([0-9]+) green", round)
            if green_cubes:
                if int(green_cubes.group(1)) > number_of_cubes["green"]:
                    game_possible = False
                    break

        if game_possible:
            running_total += game_id

print(running_total)
