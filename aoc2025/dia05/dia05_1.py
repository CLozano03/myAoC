with open("input.txt") as f:
    ranges, ingredients = f.read().split("\n\n")


rgs = []
for r in ranges.splitlines():
    st, end = r.split("-")
    rgs.append((int(st), int(end)))

print(rgs)

count_fresh = 0

for ing in ingredients.splitlines():
    for rg in rgs:
        st, end = rg
        if st <= int(ing) <= end:
            count_fresh += 1
            break

print(count_fresh)
