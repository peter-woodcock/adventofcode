with open("input.txt") as f:
    running_total = 0
    for line in f:
        numeric_characters = [chr for chr in line if chr.isnumeric()]
        running_total += int(numeric_characters[0] + numeric_characters[-1])

print(running_total)