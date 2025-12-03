with open("input.txt", "r") as file:
    lines = file.readlines()

curr = 50
count = 0
for line in lines:
    if line[0] == "L":
        curr = (curr + int(line[1:])) % 100
    else:
        curr = (curr - int(line[1:])) % 100

    if curr == 0:
        count += 1

print(count)
