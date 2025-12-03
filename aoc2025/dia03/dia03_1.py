from itertools import combinations

with open("input.txt") as f:
    lines = f.readlines()

JOLT_SIZE = 12

count = 0
for line in lines:
    numbers = [int(char) for char in line.strip()]
    max_joltage = float("-inf")

    for comb in combinations(numbers, JOLT_SIZE):
        joltage = int("".join(map(str, comb)))

        if joltage > max_joltage:
            max_joltage = joltage

    count += max_joltage

print(count)
