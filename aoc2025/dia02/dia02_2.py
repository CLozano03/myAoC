ids_range = open("input.txt").read().strip().split(",")


div = {}
# Precompute divisors
for i in range(2, 30):
    divs = []
    for j in range(1, i):
        if i % j == 0:
            divs.append(j)
    divs.sort()
    div[i] = divs

count = 0
for range_str in ids_range:
    start, end = map(int, range_str.split("-"))

    for i in range(start, end + 1):
        str_i = str(i)
        len_str = len(str_i)
        if len_str not in div:
            continue
        for n in div[len_str]:
            trozos = [str_i[x : x + n] for x in range(0, len_str, n)]

            if all(t == trozos[0] for t in trozos):
                count += i
                break

print(count)
