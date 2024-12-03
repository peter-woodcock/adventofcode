import re

running_total = 0


def get_higher_count(colour: str, current_count: int) -> int:
    given_cubes = re.search(f"([0-9]+) {colour}", round)
    return max(current_count, int(given_cubes.group(1))) if given_cubes else current_count


with open("input.txt", newline="\n") as f:
    for line in f:
        colour_counts = {"red": 0, "green": 0, "blue": 0}
        rounds = line[8:].split(";")
        for round in rounds:
            for colour in colour_counts:
                colour_counts[colour] = get_higher_count(colour, colour_counts[colour])

        running_total += colour_counts["red"] * colour_counts["green"] * colour_counts["blue"]

print(running_total)