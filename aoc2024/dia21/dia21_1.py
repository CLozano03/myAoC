from typing import List, Dict, Tuple
from itertools import product # Cartesian product
from functools import lru_cache
import heapq

FILENAME = "input.txt"
N_INTER_ROBOTS = 2

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
NUMERIC_KEYPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2)
}

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
DIRECTIONAL_KEYPAD = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

# -------------------------------------------------------------------------------
def get_paths(KEYPAD: Dict[str, Tuple[int, int]]) -> Dict[Tuple[str], List[str]]:
    '''
    Get all possible sequences from one key to another key in a keypad.
    @return: Dict[Tuple[Tuple[int]], List[str]] where the key is a tuple with the origin and destination keys and the value is a list of sequences.
    '''
    seqs_ret: Dict[Tuple[Tuple[int]], List[str]] = {}
    
    KEYPAD_COORDS = set(KEYPAD.values())
    
    for key_origin in KEYPAD.keys():
        for key_dest in KEYPAD.keys():
            if key_origin == key_dest:
                seqs_ret[(key_origin, key_dest)] = ["A"]; continue
            
            origin_x, origin_y = KEYPAD[key_origin]
            end_x, end_y = KEYPAD[key_dest]
            
            # BFS
            # Should explore all possible paths of min length from origin to destination
            best_cost: int = float('inf')
            paths: List[str] = []
            pq = [(0, (origin_x, origin_y), "")] # (cost, (x, y), path)
            
            while pq:
                cost, (cx, cy), path = heapq.heappop(pq)
                
                for dx, dy, new_move in [(0, 1, ">"), (0, -1, "<"), (1, 0, "v"), (-1, 0, "^")]:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) not in KEYPAD_COORDS: continue
                    
                    if (nx, ny) == (end_x, end_y):
                        if best_cost < cost + 1: break    
                        best_cost = cost + 1
                        paths.append(path + new_move + "A")
                    else:
                        heapq.heappush(pq, (cost + 1, (nx, ny), path + new_move))
                else: 
                    continue
                break
            seqs_ret[(key_origin, key_dest)] = paths

    return seqs_ret
    
def all_paths_for_code(code: str, paths: Dict[Tuple[Tuple[int]], List[str]]) -> List[str]:
    '''
    Get the best sequence for a code.
    @return: List[str] with the best sequence for the code.
    '''
    # Get all paths for each codedigit (starts in A)
    # 029A -> [ ['<A'], ['^A'], [''], ['vvvA']]
    # Example:  A to 0    0 to 2  2 to 9  9 to A
    paths_to_each_codedigit: List[List[str]] = [paths[(i,j)] for i, j in zip("A" + code, code)] # "A" + code to start in A
    # Cartesian product of all paths in a list
    # ['<A'], ['^A'], [''], ['vvvA'] -> ['<A', '^A', '', 'vvvA']
    return ["".join(seq) for seq in product(*paths_to_each_codedigit)]

@lru_cache(maxsize=None) # Cache the results of the function to avoid recomputing
def shortest_seq_len(path: str, n_robots: int) -> int:
    '''
    Recursive function to get the shortest sequence length for a code.
    '''
    # Base case, if there is only one robot
    # Return the sum of a way to go from each key to its next key
    if n_robots == 1:
        return sum(len(DIR_SEQUENCES[(x, y)][0]) for x, y in zip("A" + path, path))
    
    # If not, DFS for each subsequence in the current sequence, decreasing the number of robots y 1
    # Take the minimum of all the results
    length = 0
    for x, y in zip("A" + path, path):
        length += min(shortest_seq_len(subseq, n_robots - 1) for subseq in DIR_SEQUENCES[(x, y)])
    return length
    
# -------------------------------------------------------------------------------
codes: List[str] = [ line.strip() for line in open(FILENAME)]
  
# Get all possible sequences from one key to another key in each keypad
# key: [(origin, destination)]
# value: list of min paths from origin to destination
NUMERIC_SEQUENCES: Dict[Tuple[str], List[str]] = get_paths(NUMERIC_KEYPAD)
DIR_SEQUENCES: Dict[Tuple[str], List[str]] = get_paths(DIRECTIONAL_KEYPAD)

# Calculate the total complexity
total_complexity: int = 0
for code in codes:
    code_paths = all_paths_for_code(code, NUMERIC_SEQUENCES) # Get all possible paths for typing the code
    min_length = min(shortest_seq_len(path, N_INTER_ROBOTS) for path in code_paths)
    total_complexity += min_length * int(code[:-1])

print(f'Complexity: {total_complexity}')