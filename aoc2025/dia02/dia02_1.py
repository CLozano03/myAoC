ids_range = open("input.txt").read().strip().split(",")

count = 0
for range_str in ids_range:
    start, end = map(int, range_str.split("-"))

    for i in range(start, end + 1):
        str_i = str(i)
        len_str = len(str_i)

        first_half = str_i[: len_str // 2]
        second_half = str_i[len_str // 2 :]
        count += i if int(first_half) == int(second_half) else 0

print(count)
