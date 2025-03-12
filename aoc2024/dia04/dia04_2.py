from typing import Tuple

FILENAME = "input.txt"


def read_file():
    global _n_rows_matrix, _n_cols_matrix

    with open(FILENAME, "r") as file:
        lines = file.readlines()
        matrix = [list(line) for line in lines]

        # Store some matrix data
        _n_rows_matrix = len(matrix)
        _n_cols_matrix = len(matrix[0])

    return matrix


# Checks if a given pos in coordinates (i, j) belongs to the matrix
def __check_matrix_pos(coord: Tuple[int, int]) -> int:
    return (
        coord[0] >= 0
        and coord[1] >= 0
        and coord[0] < _n_rows_matrix
        and coord[1] < _n_cols_matrix
    )


# Easy way to access elements of a matrix
def el_matrix(matrix, coord):
    return matrix[coord[0]][coord[1]]


def is_X_MAS(matrix, coord: Tuple[int, int]):
    top_left = (coord[0] - 1, coord[1] - 1)
    top_right = (coord[0] - 1, coord[1] + 1)
    bottom_left = (coord[0] + 1, coord[1] - 1)
    bottom_right = (coord[0] + 1, coord[1] + 1)

    # First check out of bounds
    inside_matrix = (
        __check_matrix_pos(top_left)
        and __check_matrix_pos(top_right)
        and __check_matrix_pos(bottom_left)
        and __check_matrix_pos(bottom_right)
    )
    if not inside_matrix:
        return 0

    first_axe = (
        el_matrix(matrix, top_left) == "M"
        and el_matrix(matrix, bottom_right) == "S"
    ) or (
        el_matrix(matrix, top_left) == "S"
        and el_matrix(matrix, bottom_right) == "M"
    )
    second_axe = (
        el_matrix(matrix, top_right) == "M"
        and el_matrix(matrix, bottom_left) == "S"
    ) or (
        el_matrix(matrix, top_right) == "S"
        and el_matrix(matrix, bottom_left) == "M"
    )

    is_there_xmas = first_axe and second_axe

    if is_there_xmas:
        return 1
    else:
        return 0


def count_str_matrix(matrix):
    total_sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "A":
                continue

            total_sum += is_X_MAS(matrix, (i, j))

    return total_sum


input_matrix = read_file()  # First convert the input into a matrix of chars
res = count_str_matrix(input_matrix)  # Count all the 'X-MAS' appears in matrix

print(f"Sum of 'X-MAS': {res}")
