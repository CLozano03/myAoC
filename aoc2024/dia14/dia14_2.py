from typing import List, Tuple
import re

FILENAME = "input.txt"

X_SIZE = 101
Y_SIZE = 103


class Robot:
    def __init__(self, position: Tuple[int], velocity: Tuple[int]):
        self.position: Tuple[int] = position
        self.velocity: Tuple[int] = velocity

    def __repr__(self):
        return f"Robot({self.position}, {self.velocity})"


# -------------------------------------------------------------------------------
# Read and save in a List of List of positions and velocities
def read_file() -> List[Robot]:
    matrix = []

    with open(FILENAME, "r") as file:
        for line in file:
            p_x, p_y, v_x, v_y = map(int, re.findall(r"-?\d+", line.strip()))
            matrix.append(Robot((p_x, p_y), (v_x, v_y)))

    return matrix


def find_easter_egg(robots: List[Robot]) -> None:
    for curr_second in range(10000):
        print()
        print(curr_second)

        # Generate a grid of 0s to be printed
        grid = [[0] * X_SIZE for _ in range(Y_SIZE)]

        for robot in robots:
            x, y = robot.position
            v_x, v_y = robot.velocity

            curr_x = (x + curr_second * v_x) % X_SIZE
            curr_y = (y + curr_second * v_y) % Y_SIZE

            grid[curr_y][curr_x] = 1

        # PRINT THE GRID
        for row in grid:
            print("".join(["#" if cell == 1 else "." for cell in row]))

        print()


# -------------------------------------------------------------------------------

robots: List[Robot] = read_file()
find_easter_egg(robots)
