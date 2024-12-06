import copy
import time
from typing import List, Tuple

curr_checking_gl = None

FILENAME = "input.txt"

class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        
        self.player_pos = self.__locate_start_pos() # Store player pos
        self.player_dir = 0 # 0: Up 1: Right 2: Down 3: Right
        self.MAX_VISIT = self.n_cols * self.n_rows
        
    def next_square(self):
        if self.player_dir == 0:
            return (self.player_pos[0] - 1, self.player_pos[1])
        if self.player_dir == 1:
            return (self.player_pos[0], self.player_pos[1] + 1)
        if self.player_dir== 2:
            return (self.player_pos[0] + 1, self.player_pos[1])
        if self.player_dir == 3:
            return (self.player_pos[0], self.player_pos[1] - 1)
        
    def set_new_pos(self, coord: Tuple[int]):
        self.player_pos = coord
        
    def set_obstruction(self, coord: Tuple[int]):
        self.matrix[coord[0]][coord[1]] = '#'
    
    def void_square(self, coord: Tuple[int]):
        self.matrix[coord[0]][coord[1]] = '.'
    
    def get_el(self, coord: Tuple[int]):
        return self.matrix[coord[0]][coord[1]]
        
    def change_dir(self): # Rotates player by 90º
        self.player_dir = (self.player_dir + 1) %4
    
    def belongs_to_matrix(self, coord: Tuple[int]) -> bool:
        return coord[0] >= 0 and coord[1] >= 0 and coord[0] < self.n_rows and coord[1] < self.n_cols 
        
    def __locate_start_pos(self):
        for i, row in enumerate(self.matrix):
            for j, el in enumerate(row):
                if el == '^':
                    return (i,j)
        return None
       
# -------------------------------------------------------------------------------      
             
def read_file(): 
    with open(FILENAME, 'r') as file:
        lines = file.readlines()
        map_matrix = [list(line.strip()) for line in lines]
        
        return Map(matrix = map_matrix)
    
# Normal run with no extra obstructions for getting the posible obstructions squares
def run_normal(map: Map) -> List[Tuple[int]]:
    visited_coord = []
    start_pos_map = map.player_pos
    
    while True:
        if not map.player_pos in visited_coord:
            visited_coord.append(map.player_pos)
            
        next = map.next_square()

        if not map.belongs_to_matrix(next):
            visited_coord.remove(start_pos_map)
            return visited_coord
        if map.get_el(next) == '#':
            map.change_dir()
            continue
        
        map.set_new_pos(next)

# Run returns True if goes out of the map and there is no loop
def run(map: Map) -> bool:
    n_visited = 0
    
    while n_visited < map.MAX_VISIT:        
        next = map.next_square()
        
        if not map.belongs_to_matrix(next):
            return True
        if map.get_el(next) == '#':
            map.change_dir()
            continue
        
        n_visited += 1
        map.set_new_pos(next)

    return False        

def count_possible_obstructions(start_map: Map):
    sum_possible_obstrucions = 0
    
    mod_map = copy.deepcopy(start_map)
    possibly_affected = run_normal(mod_map)

    for curr_checking in possibly_affected:
        mod_map = copy.deepcopy(start_map)        
        mod_map.set_obstruction(curr_checking)
                
        if not run(mod_map):
            sum_possible_obstrucions += 1
        
    return sum_possible_obstrucions
    
# -------------------------------------------------------------------------------

start_map = read_file()
res = count_possible_obstructions(start_map)

print(f'Sum of possible obstructions: {res}')
