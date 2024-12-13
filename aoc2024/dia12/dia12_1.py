from typing import List, Tuple

FILENAME = "input.txt"

visited: List[Tuple[int]] = []

class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix : List[List[str]] = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        
    def get_n_neighbours(self, coord: Tuple[int], type: str) -> int:
        row, col = coord
        neighbours = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1),  # Right
        ]
        
        count = 0
        for neighbour in neighbours:
            if self.belongs_to_matrix(neighbour) and self.get_el(neighbour) == type:
                count += 1
        
        return count
    
    def get_neighbours(self, coord: Tuple[int], type: str) -> List[Tuple[int]]:
        row, col = coord
        neighbours = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1),  # Right
        ]
        
        valid_neighbours = []
        for neighbour in neighbours:
            if self.belongs_to_matrix(neighbour) and not neighbour in visited and self.get_el(neighbour) == type:
                valid_neighbours.append(neighbour)
        
        return valid_neighbours
    
    def get_el(self, coord: Tuple[int]) -> str:
        return self.matrix[coord[0]][coord[1]]
    
    def belongs_to_matrix(self, coord: Tuple[int]) -> bool:
        return coord[0] >= 0 and coord[1] >= 0 and coord[0] < self.n_rows and coord[1] < self.n_cols 


def read_file() -> Map: 
    matrix = []
    
    with open(FILENAME, 'r') as file:
        for line in file:
            matrix.append([str(d) for d in line.strip()])
    
    return Map(matrix)


def calculate_price_for_type(curr_pos: Tuple[int], type: str) -> Tuple[int, int]:
    area = 1
    perimeter = 4 - garden.get_n_neighbours(curr_pos, type)
    
    visited.append(curr_pos) # Mark as visited
    
    for neigh in garden.get_neighbours(curr_pos, type):
        if neigh not in visited:
            plus_area, plus_perimeter = calculate_price_for_type(neigh, type)
            area += plus_area
            perimeter += plus_perimeter 
    
    return area, perimeter

def calculate_price() -> int:
    price = 0
    
    for i in range(garden.n_rows):
        for j in range(garden.n_cols):
            if (i,j) not in visited:
                type = garden.get_el((i,j))
                area, perimeter = calculate_price_for_type((i,j), type)
                print(f'Calculating price for type {type} -> {area} * {perimeter} = {area*perimeter}')
                price += area * perimeter
        
    return price

# -------------------------------------------------------------------------------

garden = read_file()
price = calculate_price()

print(f'Total price: {price}')