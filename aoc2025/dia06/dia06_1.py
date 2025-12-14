with open("input.txt") as f:
    lines = f.read().splitlines()

lines_lst = []
for line in lines:
    lines_lst.append(line.split())

sum = 0

for j in range(len(lines_lst[0])):
    acc = int(lines_lst[0][j])
    op = lines_lst[4][j]

    for i in range(1, 4):
        val = int(lines_lst[i][j])

        if op == "+":
            acc += val
        elif op == "*":
            acc *= val

    sum += acc

print(sum)
