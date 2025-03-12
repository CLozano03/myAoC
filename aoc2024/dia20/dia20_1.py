from typing import List, Tuple
import heapq

FILENAME = "input.txt"


def dijkstra(
    maze, distances: List[List], start_pos: Tuple[int], end_pos: Tuple[int]
) -> Tuple[int, List[Tuple[int]]]:
    heap_queue = [(0, start_pos)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = []
    predecessors = {}  # Dictionary to store the predecessors of each position
    distances[start_pos[0]][start_pos[1]] = 0

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
                predecessors[(nx, ny)] = (c_x, c_y)
                heapq.heappush(heap_queue, (distances[nx][ny], (nx, ny)))

    path = []
    current = end_pos
    while current != start_pos:
        path.append(current)
        current = predecessors.get(current)
        if current is None:
            return -1, []
    path.append(start_pos)
    path.reverse()

    return distances[end_pos[0]][end_pos[1]], path


def count_cheatable(
    maze, path: List[Tuple[int]], distances: List[List[int]]
) -> int:
    count = 0

    for square in path:
        cx, cy = square[0], square[1]
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cx + direction[0], cy + direction[1]
            sx, sy = cx + 2 * direction[0], cy + 2 * direction[1]
            if sx < 0 or sx >= M_SIZE or sy < 0 or sy >= M_SIZE:
                continue

            if maze[nx][ny] != "#":
                continue
            if maze[sx][sy] != "." and maze[sx][sy] != "E":
                continue

            if distances[sx][sy] - distances[cx][cy] >= MIN_SAVE + 2:
                count += 1

    return count


# -------------------------------------------------------------------------------
# Read the input file
with open(FILENAME, "r") as file:
    grid: List[List[str]] = [[str(n) for n in line.strip()] for line in file]

M_SIZE = len(grid)
MIN_SAVE = 100

# Find the start and end positions
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "E":
            end = (i, j)

distances: List[List[str]] = [
    [-1 for _ in range(M_SIZE)] for _ in range(M_SIZE)
]
# Calculate the shortest path from dijkstra algorithm. Actually there is only one path
_, path = dijkstra(grid, distances, start, end)

cheats_that_worth = count_cheatable(grid, path, distances)
print(f"Cheats that save at least {MIN_SAVE} picoseconds: {cheats_that_worth}")
