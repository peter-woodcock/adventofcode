import re

running_total = 0

with open("input.txt", newline="\n") as f:
    for line in f:
        highest_red = 0
        highest_blue = 0
        highest_green = 0

        rounds = line[8:].split(";")
        for round in rounds:
            blue_cubes = re.search("([0-9]+) blue", round)
            if blue_cubes and int(blue_cubes.group(1)) > highest_blue:
                highest_blue = int(blue_cubes.group(1))

            red_cubes = re.search("([0-9]+) red", round)
            if red_cubes and int(red_cubes.group(1)) > highest_red:
                highest_red = int(red_cubes.group(1))

            green_cubes = re.search("([0-9]+) green", round)
            if green_cubes and int(green_cubes.group(1)) > highest_green:
                highest_green = int(green_cubes.group(1))

        running_total += highest_red * highest_blue * highest_green

print(running_total)