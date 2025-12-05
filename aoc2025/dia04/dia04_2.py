import copy

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]


def forklits(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    count = 0
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                continue
            sum = 0

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue

                    ni, nj = i + di, j + dj

                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == "@":
                            sum += 1

            if sum < 4:
                count += 1
                new_grid[i][j] = "."

    return count, new_grid


total = 0
extra = 1

while extra != 0:
    extra, grid = forklits(grid)
    total += extra

print(total)
