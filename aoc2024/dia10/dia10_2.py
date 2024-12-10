from typing import List, Tuple

FILENAME = "input.txt"

class Map:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        
    def get_next_pos_list(self, curr_pos: Tuple[int]):
        return [ (curr_pos[0] - 1, curr_pos[1]),
                 (curr_pos[0], curr_pos[1] + 1),
                 (curr_pos[0] + 1, curr_pos[1]),
                 (curr_pos[0], curr_pos[1] - 1) ]
        
    
    def get_el(self, coord: Tuple[int]):
        return self.matrix[coord[0]][coord[1]]
    
    def belongs_to_matrix(self, coord: Tuple[int]) -> bool:
        return coord[0] >= 0 and coord[1] >= 0 and coord[0] < self.n_rows and coord[1] < self.n_cols 
        
    def get_start_pos_list(self) -> List[Tuple[int]]:
        ret = []
        
        for i, row in enumerate(self.matrix):
            for j, el in enumerate(row):
                if el == 0:
                    ret.append((i,j))
                    
        return ret


def read_file() -> Map: 
    matrix = []
    
    with open(FILENAME, 'r') as file:
        for line in file:
            matrix.append([int(d) for d in line.strip()])
    
    return Map(matrix)

def calculate_trailhead_score_from_position(matrix: Map, curr_coord: Tuple[int], height: int) -> int:
    
    if height == 9: return 1
    trailhead_sum = 0
    next_pos_list = matrix.get_next_pos_list(curr_coord) # Get next positions
    
    for pos in next_pos_list:
        if matrix.belongs_to_matrix(pos) and height + 1 == matrix.get_el(pos):
            # If the position is valid and the height is the next one, then we can go there
            trailhead_sum += calculate_trailhead_score_from_position(matrix, pos, height + 1)
            
    return trailhead_sum
    
def sum_all_trailheads(matrix: Map) -> int:
    trailheads_sum = 0
    start_pos_list = matrix.get_start_pos_list()
    
    for start_pos in start_pos_list:
        trailheads_sum += calculate_trailhead_score_from_position(matrix, start_pos, 0)
        
    return trailheads_sum

# -------------------------------------------------------------------------------

map_start = read_file()
res = sum_all_trailheads(map_start)

print(f'Trailheads sum: {res}')