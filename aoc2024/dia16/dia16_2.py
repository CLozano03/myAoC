from typing import List, Tuple, Dict, Set
from collections import defaultdict, deque
import heapq
 
FILENAME = "input.txt"

# Dijkstra algorithm, now with directions.
# # Returns the number of tiles that form part of the shortest path
def dijkstra(maze, start_pos: Tuple[int], end_pos: Tuple[int]) -> Tuple[int, int]:
    
    heap_queue = [(0, start_pos, (0,1))] # (distance, position, direction) # DIR starts as EAST
    predecessors: Dict[Tuple[int], Set] = defaultdict(lambda: set()) # Dictionary to store the predecessors of each position
    
    distances = defaultdict(lambda: float('inf')) # Dictionary to store the distances to each position (with direction)
    distances[(start_pos[0], start_pos[1], (0,1))] = 0 # Distance to start position is 0

    best_cost = float('inf')
    final_states = set()

    while heap_queue:
        dist, (cx, cy), dir = heapq.heappop(heap_queue)
        
        # Not improving previous best cost -> next position        
        if dist > distances[(cx, cy, dir)]: continue

        # REACHING THE END
        if (cx,cy) == end_pos:
            # I have arrived to the end with a higher cost than the best one
            if dist > best_cost: break
                        
            best_cost = dist
            final_states.add((cx, cy, dir))
         
        # Check all possible directions 
        for distance_to_next, dx, dy in [(1, dir[0], dir[1]), (1001, dir[1], -dir[0]), (1001, -dir[1], dir[0])]:
            nx, ny = cx + dx, cy + dy # Calculate next position
            
            # If the next position is a wall or already visited -> next position
            if maze[nx][ny] == '#': continue
            
            new_dist = dist + distance_to_next    
            
            # If the distance to the next position is less than the current distance
            # Update the distance and add the next position to the queue
            prev_lowest = distances[(nx, ny, (dx, dy))]
            if new_dist > prev_lowest: continue
            if new_dist < prev_lowest:
                predecessors[(nx, ny, (dx, dy))].clear()        
                distances[(nx, ny, (dx, dy))] = new_dist
        
            predecessors[(nx, ny, (dx, dy))].add((cx, cy, dir))
            heapq.heappush(heap_queue, (new_dist, (nx, ny), (dx, dy)))
            
    # BACKTRACKING PROCESS
    states = deque(final_states)    
    visited = set(final_states)
    
    while states: 
        state = states.popleft()
        for pred in predecessors[state]:
            if pred in visited: continue
            states.append(pred)
            visited.add(pred)    
    
    return len({(i, j) for i, j, _ in visited})

# -------------------------------------------------------------------------------
with open(FILENAME) as file:      
    grid: List[List[str]] = [list(line.strip()) for line in file]

# Find start and end positions
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)  # start position
        if grid[i][j] == 'E':
            end = (i, j)    # end position

tiles = dijkstra(grid, start, end)
print(f'Tiles, that form part of shortest path: {tiles}')