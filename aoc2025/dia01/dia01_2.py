with open("input.txt", "r") as file:
    lines = file.readlines()

count = 0
pos = 50
for line in lines:
    move = int(line[1:])
    clicks = move // 100
    disp = move % 100

    if line[0] == "R":
        next_pos = pos + disp
        if pos != 0 and next_pos >= 100:
            count += 1
    else:
        next_pos = pos - disp
        if pos != 0 and next_pos <= 0:
            count += 1

    # if next_pos == 0:
    #     count += 1

    count += clicks

    pos = next_pos % 100
    # print(pos)
    # print(f"Count: {count}")


print(count)
