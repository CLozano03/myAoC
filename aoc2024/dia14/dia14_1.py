from typing import List, Tuple
import re

FILENAME = "input.txt"

N_SECONDS = 100
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


def calculate_safety_factor(robots: List[Robot]) -> int:
    cuadrants_count = {0: 0, 1: 0, 2: 0, 3: 0}

    for robot in robots:
        x, y = robot.position
        v_x, v_y = robot.velocity

        # Calculate the position of the robot after N_SECONDS
        last_x = (x + N_SECONDS * v_x) % X_SIZE
        last_y = (y + N_SECONDS * v_y) % Y_SIZE

        # If the robot is in the middle of the grid, it doesn't count as being in any cuadrant
        if last_x == X_SIZE // 2 or last_y == Y_SIZE // 2:
            continue

        if last_x < X_SIZE // 2:
            if last_y < Y_SIZE // 2:
                cuadrants_count[0] += 1
            else:
                cuadrants_count[1] += 1
        else:
            if last_y < Y_SIZE // 2:
                cuadrants_count[2] += 1
            else:
                cuadrants_count[3] += 1

    return (
        cuadrants_count[0]
        * cuadrants_count[1]
        * cuadrants_count[2]
        * cuadrants_count[3]
    )


# -------------------------------------------------------------------------------

robots: List[Robot] = read_file()
safety_factor: int = calculate_safety_factor(robots)

print(f"Safety_factor: {safety_factor}")
