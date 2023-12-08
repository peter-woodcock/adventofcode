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

running_total = 0

with open("input.txt") as f:
    for line in f:

        first_digit = ''
        non_numeric_characters = ''

        for chr in line:

            if chr.isnumeric():
                first_digit = chr

            non_numeric_characters += chr

            for digit in valid_digits_as_text:
                if digit in non_numeric_characters:
                    first_digit = valid_digits[digit]

            if first_digit:
                break

        last_digit = ''
        non_numeric_characters = ''

        for chr in reversed(line):

            if chr.isnumeric():
                last_digit = chr

            non_numeric_characters = chr + non_numeric_characters

            for digit in valid_digits_as_text:
                if digit in non_numeric_characters:
                    last_digit = valid_digits[digit]

            if last_digit:
                break

        running_total += int(first_digit + last_digit)


print(running_total)
