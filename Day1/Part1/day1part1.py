with open("../input.txt") as f:
    running_total = 0
    for line in f:
        numeric_characters = [chr for chr in line if chr.isnumeric()]
        first_and_last_character = numeric_characters[0] + numeric_characters[-1]
        running_total += int(first_and_last_character)

print(running_total)