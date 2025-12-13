from functools import lru_cache

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

st = (-1, -1)

# Find the starting position 'S' in the grid
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        st = (0, i)


@lru_cache(None)
def split(pos):
    global timelines

    x, y = pos
    if x + 1 >= len(grid):
        return 1

    counter_acc = 0

    if grid[x + 1][y] == ".":
        counter_acc = split((x + 1, y))
    if grid[x + 1][y] == "^":
        if y + 1 < len(grid[0]) and (x + 1, y + 1):
            counter_acc += split((x + 1, y + 1))
        if y - 1 >= 0 and (x + 1, y - 1):
            counter_acc += split((x + 1, y - 1))

    return counter_acc


print(split(st))
