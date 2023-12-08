from typing import Literal

def find_digit(line: str, digit_position: Literal['first', 'last']) -> str:
    valid_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    valid_digits_as_text = valid_digits.keys()

    digit = ''
    non_numeric_characters = ''

    if digit_position == 'last':
        line = reversed(line)

    for chr in line:

        if chr.isnumeric():
            return chr

        if digit_position == 'last':
            non_numeric_characters = chr + non_numeric_characters
        else:
            non_numeric_characters += chr

        for valid_digit in valid_digits_as_text:
            if valid_digit in non_numeric_characters:
                return valid_digits[valid_digit]


running_total = 0

with open("input.txt") as f:
    for line in f:
        running_total += int(find_digit(line, 'first') + find_digit(line, 'last'))

print(running_total)
