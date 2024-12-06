from typing import List, Tuple

FILENAME = "input.txt"

visited_coord = []

class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        
        self.player_pos = self.__locate_start_pos() # Store player pos
        self.player_dir = 0 # 0: Up 1: Right 2: Down 3: Right
        
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
        map_matrix = [list(line) for line in lines]
        
        return Map(matrix = map_matrix)

# Return number of unique visited places
def run(map: Map):
    n_visited = 1 # Counting start pos
    
    while True:
        next = map.next_square()

        if not map.belongs_to_matrix(next):
            return n_visited
        if map.get_el(next) == '#':
            map.change_dir()
            continue
        if next not in visited_coord:
            visited_coord.append(next)
            n_visited += 1
        
        map.set_new_pos(next)

# -------------------------------------------------------------------------------

map = read_file()
res = run(map)

print(f'Sum of middle pages of correctly-ordered updates: {res}')

      
                    