from typing import List, Tuple

FILENAME = "input.txt"

checked_freqs = ["."]
antinodes_coords = []  # List for not adding twice same antinode coord


class Map:
    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        self.n_rows = 50
        self.n_cols = 50

    def get_el(self, coord: Tuple[int]) -> str:
        return self.matrix[coord[0]][coord[1]]

    def belongs_to_matrix(self, coord: Tuple[int]) -> bool:
        return (
            coord[0] >= 0
            and coord[1] >= 0
            and coord[0] < self.n_rows
            and coord[1] < self.n_cols
        )

    def locate_all_char(self, char: str):
        coord_res = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.get_el((i, j)) == char:
                    coord_res.append((i, j))

        return coord_res

    def get_antinode_pos(
        self, coord1: Tuple[int], coord2: Tuple[int]
    ) -> List[Tuple[int]]:
        distance = (coord1[0] - coord2[0], coord1[1] - coord2[1])
        return [
            (coord1[0] + distance[0], coord1[1] + distance[1]),
            (coord2[0] - distance[0], coord2[1] - distance[1]),
        ]

    def locate_antinodes_for_el(self, freqs: List[str]):
        sum_antinodes_for_freq = 0

        for i in range(len(freqs) - 1):
            for j in range(i + 1, len(freqs)):
                freq1, freq2 = freqs[i], freqs[j]
                possible_antinodes = self.get_antinode_pos(freq1, freq2)

                for possible_antinode in possible_antinodes:
                    # Check if it is really an antinode
                    if (
                        self.belongs_to_matrix(possible_antinode)
                        and not possible_antinode in antinodes_coords
                    ):
                        antinodes_coords.append(possible_antinode)
                        sum_antinodes_for_freq += 1

        return sum_antinodes_for_freq


# -------------------------------------------------------------------------------


def read_file():
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        map_matrix = [list(line) for line in lines]

        return Map(matrix=map_matrix)


def calculate_antinodes(matrix: Map):
    total_antinodes = 0

    for i in range(matrix.n_rows):
        for j in range(matrix.n_cols):
            curr_el = matrix.get_el((i, j))

            if not curr_el in checked_freqs:
                checked_freqs.append(
                    curr_el
                )  # Dont check twice the same frequency

                all_pos_freq = matrix.locate_all_char(curr_el)
                total_antinodes += matrix.locate_antinodes_for_el(all_pos_freq)

    return total_antinodes


# -------------------------------------------------------------------------------

antennas_map = read_file()
res = calculate_antinodes(antennas_map)

print(f"Total num of antinodes: {res}")
