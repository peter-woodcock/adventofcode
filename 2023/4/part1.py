import re

running_total = 0

with open("input.txt") as f:
    for line in f:
        winning_numbers = list(filter(None, re.search(": (.*) \|", line).group(1).split(' ')))
        ticket_numbers = list(filter(None, re.search("\| (.*)", line).group(1).split(' ')))

        matching_numbers = set(winning_numbers) & set(ticket_numbers)
        if matching_numbers:
            running_total += 2 ** (len(matching_numbers) - 1)

print(running_total)