import re

pattern = re.compile("mul\((\d*),(\d*)\)|(don't\(\))|(do\(\))")

with open("input.txt") as f:
    memory = f.read()

matches = (pattern.finditer(memory))

enabled = True
total = 0
for match in matches:
    if match.group() == "do()":
        enabled = True
        continue
    if match.group() == "don't()":
        enabled = False
    if not enabled:
        continue
    if enabled:
        total += int((match.group().split(",")[0].lstrip("mul("))) * int((match.group().split(",")[1].rstrip(")")))

print(total)
