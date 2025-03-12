from typing import List, Tuple
import re
import heapq

FILENAME = "input.txt"
M_SIZE = 71

coords: List[Tuple[int]] = []

for line in open(FILENAME):
    match = re.compile(r"(\d+),(\d+)").match(line.strip())
    if match:
        coords.append(tuple(map(int, match.groups())))


def dijkstra(
    maze, distances: List[List], start_pos: Tuple[int], end_pos: Tuple[int]
) -> int:
    heap_queue = [(0, start_pos)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = []

    while heap_queue:
        _, (c_x, c_y) = heapq.heappop(heap_queue)
        curr_dist = distances[c_x][c_y]

        visited.append((c_x, c_y))

        if grid[c_x][c_y] == end_pos:
            continue

        for dx, dy in directions:
            nx, ny = c_x + dx, c_y + dy  # Calculate next position
            # Chack matrix borders
            if nx < 0 or nx >= M_SIZE or ny < 0 or ny >= M_SIZE:
                continue
            # If the next position is a wall or already visited -> next position
            if maze[nx][ny] == "#" or (nx, ny) in visited:
                continue

            # If the distance to the next position is less than the current distance
            # Update the distance and add the next position to the queue
            if distances[nx][ny] == -1 or distances[nx][ny] > curr_dist + 1:
                distances[nx][ny] = curr_dist + 1
                heapq.heappush(heap_queue, (distances[nx][ny], (nx, ny)))

    return distances[end_pos[0]][end_pos[1]]


# -------------------------------------------------------------------------------
grid: List[List[str]] = [["." for _ in range(M_SIZE)] for _ in range(M_SIZE)]
distances: List[List[str]] = [
    [-1 for _ in range(M_SIZE)] for _ in range(M_SIZE)
]

# Add all the corrupted memory coords to grid
for it in range(1024):
    i, j = coords[it]
    grid[i][j] = "#"

distances[0][0] = 0
min_dist = dijkstra(grid, distances, (0, 0), (70, 70))

print(f"Min distance: {min_dist}")
