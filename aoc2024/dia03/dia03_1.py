import re

FILENAME = "input.txt"


def read_file():
    with open(FILENAME, "r") as file:
        lines = file.readlines()

    return lines


def multiply_in_regex(file_lines):
    res = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"

    for line in file_lines:
        for match in re.finditer(regex, line):
            num1, num2 = int(match.group(1)), int(match.group(2))
            res += num1 * num2

    return res


# -------------------------------------------------------------------------------

file_lines = read_file()
res = multiply_in_regex(file_lines)

print(f"Sum of muls: {res}")
