from typing import List, Tuple
import heapq

FILENAME = "input.txt"

with open(FILENAME) as file:
    grid: List[List[str]] = [list(line.strip()) for line in file]

distances = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)  # start position
            distances[i][j] = 0
        if grid[i][j] == "E":
            end = (i, j)


# Dir is True if the movement is vertical . False if horizontal
def dijkstra(maze, distances: List[List], start_pos: Tuple[int]) -> int:
    heap_queue = [(0, start_pos, False)]
    directions = [
        (-1, 0, True),
        (1, 0, True),
        (0, -1, False),
        (0, 1, False),
    ]  # Up, Down, Left, Right

    while heap_queue:
        _, (c_x, c_y), dir_is_vertical = heapq.heappop(heap_queue)
        curr_dist = distances[c_x][c_y]

        if grid[c_x][c_y] == end:
            continue

        for dx, dy, new_dir in directions:
            nx, ny = c_x + dx, c_y + dy  # Calculate next position
            # If the next position is a wall or already visited -> next position
            if maze[nx][ny] == "#":
                continue

            # Calculate dinamic distance through the maze
            distance_to_next = 1 if dir_is_vertical == new_dir else 1001

            # If the distance to the next position is less than the current distance
            # Update the distance and add the next position to the queue
            if (
                distances[nx][ny] == -1
                or distances[nx][ny] > curr_dist + distance_to_next
            ):
                distances[nx][ny] = curr_dist + distance_to_next
                heapq.heappush(
                    heap_queue, (distances[nx][ny], (nx, ny), new_dir)
                )

    return distances[end[0]][end[1]]


# -------------------------------------------------------------------------------

shortest_path_distance = dijkstra(grid, distances, start)
print(f"Shortest_path_distance: {shortest_path_distance}")
