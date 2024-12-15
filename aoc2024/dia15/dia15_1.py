from typing import List, Tuple

FILENAME = "input.txt"

class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        
        self.player_pos = self.__locate_start_pos() # Store player pos
    
    def __locate_start_pos(self):
        for i, row in enumerate(self.matrix):
            for j, el in enumerate(row):
                if el == '@':
                    return (i,j)
        return None

    def next_square(self, coord: Tuple[int], dir: int) -> Tuple[int]:
        if dir == 0: # UP
            return (coord[0] - 1, coord[1])
        elif dir == 1: # RIGHT
            return (coord[0], coord[1] + 1)
        elif dir == 2: # DOWN
            return (coord[0] + 1, coord[1])
        else: # LEFT
            return (coord[0], coord[1] - 1)
        
    def move(self, coord: Tuple[int], dir: int) -> None:
        new_pos = self.next_square(coord, dir)
        
        if self.get_el(new_pos) == '#':
            return
        if self.get_el(new_pos) == '.':
                self.set_new_el(self.player_pos, el='.')
                self.player_pos = new_pos
                self.set_new_el(new_pos, el='@')
        else:
            first_box_pos = new_pos
            while self.get_el(new_pos) == 'O':
                new_pos = self.next_square(new_pos, dir)
            if self.get_el(new_pos) == '#':
                return # Box can't be moved
            # empty square
            else:
                self.set_new_el(self.player_pos, el='.')
                self.player_pos = first_box_pos
                self.set_new_el(first_box_pos, el='@')
                
                self.set_new_el(new_pos, el='O')
        
    def set_new_el(self, coord: Tuple[int], el: str):
        self.matrix[coord[0]][coord[1]] = el   
    
    def get_el(self, coord: Tuple[int]):
        return self.matrix[coord[0]][coord[1]]

# -------------------------------------------------------------------------------
   
def read_file() -> Tuple[Map, List[str]]:
    movements: List[str] = []
    matrix = []
    
    with open(FILENAME, 'r') as file:
        parts = file.read().split('\n\n')
        map_str = parts[0]
        mov_str = parts[1].strip().replace('\n', '')
        
        for i in mov_str:
            movements.append(i)
        
        for i, row in enumerate(map_str.split('\n')):
            matrix.append(list(row))
        warehouse = Map(matrix)
        
    return warehouse, movements

def execute_movements(warehouse: Map, movements: List[str]) -> None:
    for movement in movements:
        if movement == '^':
            warehouse.move(warehouse.player_pos, 0)
        elif movement == '>':
            warehouse.move(warehouse.player_pos, 1)
        elif movement == 'v':
            warehouse.move(warehouse.player_pos, 2)
        else:
            warehouse.move(warehouse.player_pos, 3)
    
def calculate_gps_sum(warehouse: Map) -> int:
    sum_ret = 0
    
    for i, row in enumerate(warehouse.matrix):
        for j, el in enumerate(row):
            if el == 'O':
                sum_ret += 100 * i + j

    return sum_ret
    
# -------------------------------------------------------------------------------
warehouse: Map = None
movements: List[str] = None
warehouse, movements = read_file()

execute_movements(warehouse, movements)
sum_gps = calculate_gps_sum(warehouse)

print(f'GPS coordinates Sum: {sum_gps}')
