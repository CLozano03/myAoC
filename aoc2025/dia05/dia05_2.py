with open("input.txt") as f:
    ranges, _ = f.read().split("\n\n")


rgs = []
for r in ranges.splitlines():
    st, end = r.split("-")

    rgs.append((int(st), int(end)))

rgs.sort()

union_rgs = [rgs[0]]

for st, end in rgs[1:]:
    last_st, last_end = union_rgs[-1]

    if st <= last_end + 1:
        union_rgs[-1] = (last_st, max(last_end, end))
    else:
        union_rgs.append((st, end))


fresh_count = 0
for st, end in union_rgs:
    fresh_count += end - st + 1

print(fresh_count)
