from typing import List, Tuple

FILENAME = "input.txt"


class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

        self.player_pos = self.__locate_start_pos()  # Store player pos

    def __locate_start_pos(self):
        for i, row in enumerate(self.matrix):
            for j, el in enumerate(row):
                if el == "@":
                    return (i, j)
        return None

    def get_el(self, coord: Tuple[int]):
        return self.matrix[coord[0]][coord[1]]

    def set_el(self, coord: Tuple[int], el: str):
        self.matrix[coord[0]][coord[1]] = el


# -------------------------------------------------------------------------------


def read_file() -> Tuple[Map, List[str]]:
    with open(FILENAME, "r") as file:
        map_str, mov_str = file.read().split("\n\n")

        # Expand the map to double size with the new objects
        new_objects = {"O": "[]", "@": "@.", "#": "##", ".": ".."}
        warehouse = Map(
            [
                list("".join(new_objects[c] for c in row))
                for row in map_str.splitlines()
            ]
        )

        movements = mov_str.replace("\n", "")

    return warehouse, movements


def execute_movements(warehouse: Map, movements: List[str]) -> None:
    for movement in movements:
        dir_horizontal = -1 if movement == "<" else 1 if movement == ">" else 0
        dir_vertical = -1 if movement == "^" else 1 if movement == "v" else 0
        to_move = [warehouse.player_pos]

        # Key part of this problem -> Python allows to iterate over a list and modify it at the same time
        for moving in to_move:
            new_pos = (moving[0] + dir_vertical, moving[1] + dir_horizontal)
            if new_pos in to_move:
                continue  # avoid adding the same position twice

            curr_el = warehouse.get_el(new_pos)
            move_allowed = True

            if curr_el == "#":
                move_allowed = False
                break
            elif curr_el == "[":
                to_move.append(new_pos)
                to_move.append((new_pos[0], new_pos[1] + 1))
            elif curr_el == "]":
                to_move.append(new_pos)
                to_move.append((new_pos[0], new_pos[1] - 1))

        if not move_allowed:
            continue

        # Move
        warehouse_copy = [row[:] for row in warehouse.matrix]

        for mov_x, mov_y in to_move[1:]:
            warehouse.set_el((mov_x, mov_y), ".")
        for mov_x, mov_y in to_move[1:]:
            warehouse.set_el(
                (mov_x + dir_vertical, mov_y + dir_horizontal),
                warehouse_copy[mov_x][mov_y],
            )

        # Set new player pos after moving
        warehouse.set_el(warehouse.player_pos, ".")
        warehouse.player_pos = (
            warehouse.player_pos[0] + dir_vertical,
            warehouse.player_pos[1] + dir_horizontal,
        )
        warehouse.set_el(warehouse.player_pos, "@")


def calculate_gps_sum(warehouse: Map) -> int:
    sum_ret = 0

    for i, row in enumerate(warehouse.matrix):
        for j, el in enumerate(row):
            if el == "[":
                sum_ret += 100 * i + j

    return sum_ret


# -------------------------------------------------------------------------------
warehouse: Map = None
movements: List[str] = None
warehouse, movements = read_file()

execute_movements(warehouse, movements)
sum_gps = calculate_gps_sum(warehouse)

print(f"GPS coordinates Sum: {sum_gps}")
