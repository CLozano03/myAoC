with open("input.txt") as f:
    lines = f.readlines()

JOLT_SIZE = 12

count = 0
for line in lines:
    numbers = [int(char) for char in line.strip()]
    str_acc = ""

    index_start = 0
    for i in range(JOLT_SIZE):
        digits_needed_after = JOLT_SIZE - 1 - i
        search_limit = len(numbers) - digits_needed_after
        window = numbers[index_start:search_limit]
        max_val = max(window)
        relative_idx = window.index(max_val)
        index_start += relative_idx + 1

        str_acc += str(max_val)

    count += int(str_acc)

print(count)
