with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

st = (-1, -1)

# Find the starting position 'S' in the grid
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        st = (0, i)

split_count = 0
visited = set()


def split(pos):
    if pos in visited:
        return

    visited.add(pos)

    global split_count
    x, y = pos

    if x + 1 >= len(grid) or y + 1 >= len(grid[0]) or y - 1 < 0:
        return

    if grid[x + 1][y] == ".":
        split((x + 1, y))
    if grid[x + 1][y] == "^":
        split_count += 1
        split((x + 1, y - 1))
        split((x + 1, y + 1))


split(st)
print(split_count)
