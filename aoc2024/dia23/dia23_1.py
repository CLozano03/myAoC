from typing import List, Dict, Set
from collections import defaultdict
from itertools import combinations

FILENAME = "input.txt"
CONNECTIONS_MAX_LEN = 3
STARTING_WITH = "t"

# Make a list of sets with len CONNECTIONS_MAX_LEN of computers interconnected between them
def interconnected_computers(connections: Dict[str, List[str]]) -> List[Set[str]]:
    ret = []
    computers = list(connections.keys())
    
    for combo in combinations(computers, CONNECTIONS_MAX_LEN):
        clique = set(combo)
        if len(clique) != CONNECTIONS_MAX_LEN: continue # Skip if the clique is not the desired length
        
        # Check if all nodes in the clique are connected between them
        if all(other in connections[node] for node in clique for other in clique if other != node):
            ret.append(clique)
    
    return ret

# -------------------------------------------------------------------------------
connections: Dict[str, List[str]] = defaultdict(list)

for line in open(FILENAME):
    k, v = line.strip().split("-")
    connections[k].append(v)
    connections[v].append(k)

connected: List[Set[str]] = interconnected_computers(connections)
total_starts_with_t = sum (1 for clique in connected if any(node.startswith(STARTING_WITH) for node in clique))

print(f'N of seq of len {CONNECTIONS_MAX_LEN} that at least one starts with \'{STARTING_WITH}\': {total_starts_with_t}')