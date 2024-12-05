from typing import Tuple

FILENAME = "input.txt"
NUM_DIRS = 8
string_aim = "XMAS"

_n_rows_matrix = None
_n_cols_matrix = None

'''
    Dirs: 
    1 2 3
    4   5
    6 7 8
    
'''

def read_file():
    global _n_rows_matrix, _n_cols_matrix 
    
    with open(FILENAME, 'r') as file:
        lines = file.readlines()
        matrix = [list(line) for line in lines]
        
         # Store some matrix data
        _n_rows_matrix = len(matrix); _n_cols_matrix = len(matrix[0])
        
    return matrix

# Checks if a given pos in coordinates (i, j) belongs to the matrix
def __check_matrix_pos(coord: Tuple[int, int]) -> int:
    return coord[0] >= 0 and coord[1] >= 0 and coord[0] < _n_rows_matrix and coord[1] < _n_cols_matrix 

def solve_dir(coord: Tuple[int, int], num_dir: int):
    if num_dir == 1:
        return (coord[0] - 1, coord[1] - 1)
    if num_dir == 2:
        return (coord[0] - 1, coord[1])
    if num_dir == 3:
        return (coord[0] - 1, coord[1] + 1)
    if num_dir == 4:
        return (coord[0], coord[1] - 1)
    if num_dir == 5:
        return (coord[0], coord[1] + 1)
    if num_dir == 6:
        return (coord[0] + 1, coord[1] - 1)
    if num_dir == 7:
        return (coord[0] + 1, coord[1])
    if num_dir == 8:
        return (coord[0] + 1, coord[1] + 1)
    
def find_from_dir(matrix, dir: int, coord: Tuple[int, int]):
    '''
    Given the matrix, a dir and a coordinate returns 1 if completes in that dir the string_aim
    '''
    coord_aux = coord
    
    for i in range(1, len(string_aim)):
        coord_aux = solve_dir(coord_aux, dir)

        if (not __check_matrix_pos(coord_aux)) or (matrix[coord_aux[0]][coord_aux[1]] != string_aim[i]):
            return 0
    
    return 1
    

def count_str_matrix(matrix):
    total_sum = 0    
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if matrix[i][j] != string_aim[0]:
                continue
            
            for d in range(1, NUM_DIRS + 1):
                total_sum += find_from_dir(matrix, d, (i, j))
         
    return total_sum       


input_matrix = read_file() # First convert the input into a matrix of chars
res = count_str_matrix(input_matrix) # Count all the 'XMAS' appears in matrix

print(f'Sum of \'XMAS\': {res}')