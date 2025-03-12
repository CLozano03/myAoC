from typing import List, Tuple, Dict, Set
from collections import defaultdict

FILENAME = "input.txt"
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix: List[List[str]] = matrix
        self.n_rows: int = len(matrix)
        self.n_cols: int = len(matrix[0])
        self.coord_id: Dict[Tuple[int], int] = {}
        self.id_coord: Dict[int, Set[Tuple[int]]] = defaultdict(set)

        # Assign an id to each region
        id = 0
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if (i, j) not in self.coord_id:
                    self.__dfs_for_region_id((i, j), self.matrix[i][j], id)
                    id += 1

        # Assign all the coordinates to each region
        for coord, id in self.coord_id.items():
            self.id_coord[id].add(coord)

    def garden_price(self) -> int:
        total_price = 0

        # Calculate the price for each region
        for _, coords in self.id_coord.items():
            perim_coords = set()
            area = len(coords)

            # First detect all the perimeter coordinates for the region
            for coord in coords:
                x, y = coord
                neighbours = [(x + dir[0], y + dir[1]) for dir in DIRS]
                for neighbour in neighbours:
                    if (
                        neighbour[0] not in range(self.n_rows)
                        or neighbour[1] not in range(self.n_cols)
                        or neighbour not in coords
                    ):
                        perim_coords.add(
                            (coord, neighbour)
                        )  # Add the perimeter coordinates

            total_price += area * len(perim_coords)

        return total_price

    # Recursive function to assign an id to each region
    def __dfs_for_region_id(
        self, coord: Tuple[int], letter: str, region_id: int
    ):
        x, y = coord
        if (
            x not in range(self.n_rows)
            or y not in range(self.n_cols)
            or self.matrix[x][y] != letter
        ):
            return
        if coord in self.coord_id:
            return
        if self.matrix[x][y] == letter:
            self.coord_id[coord] = region_id
            for dir in DIRS:
                self.__dfs_for_region_id(
                    (x + dir[0], y + dir[1]), letter, region_id
                )


# -------------------------------------------------------------------------------
with open(FILENAME, "r") as file:
    matrix = [list(line) for line in file.read().splitlines()]

garden = Map(matrix)
price = garden.garden_price()

print(f"Total price: {price}")
