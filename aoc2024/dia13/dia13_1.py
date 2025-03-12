from typing import List, Tuple
import math

FILENAME = "input.txt"


class Machine:
    def __init__(
        self, button_a: Tuple[int], button_b: Tuple[int], prize: Tuple[int]
    ):
        self.button_a: Tuple[int] = button_a
        self.button_b: Tuple[int] = button_b
        self.prize: Tuple[int] = prize

    def __repr__(self):
        return f"Machine(Button A: {self.button_a}, Button B: {self.button_b}, Prize: {self.prize})"

    def get_prize_X(self) -> int:
        return self.prize[0]

    def get_prize_Y(self) -> int:
        return self.prize[1]

    def get_button_a_X(self) -> int:
        return self.button_a[0]

    def get_button_a_Y(self) -> int:
        return self.button_a[1]

    def get_button_b_X(self) -> int:
        return self.button_b[0]

    def get_button_b_Y(self) -> int:
        return self.button_b[1]

    def solvable(self) -> bool:
        # Calculate if solvable with integers with gcd
        # If the prize is not divisible by the gcd of the other two numbers, it's not solvable
        gcd_1 = math.gcd(
            self.button_a[0], self.button_b[0]
        )  # Greatest common divisor
        solvable1 = self.prize[0] % gcd_1 == 0
        gcd_2 = math.gcd(
            self.button_a[1], self.button_b[1]
        )  # Greatest common divisor
        solvable2 = self.prize[1] % gcd_2 == 0

        return solvable1 and solvable2


# -------------------------------------------------------------------------------


def read_file():
    machines = []
    with open(FILENAME, "r") as file:
        lines = file.readlines()

        button_a = button_b = prize = None
        for line in lines:
            line = line.strip()
            if line.startswith("Button A:"):
                button_a = parse_values(line)
            elif line.startswith("Button B:"):
                button_b = parse_values(line)
            elif line.startswith("Prize:"):
                prize = parse_values(line)

            if button_a and button_b and prize:
                machines.append(Machine(button_a, button_b, prize))
                button_a = button_b = prize = None  # Next machine

    return machines


def parse_values(line: str) -> Tuple[int]:
    parts = line.split(":")[1].split(",")

    if line.startswith("Prize:"):
        x_val: int = int(parts[0].strip().split("=")[1])
        y_val: int = int(parts[1].strip().split("=")[1])
    else:
        x_val: int = int(parts[0].strip().split("+")[1])
        y_val: int = int(parts[1].strip().split("+")[1])

    return x_val, y_val


def calculate_tokens(machine: Machine) -> int:
    if not machine.solvable():
        return 0

    # Brute force to find the solution
    for i in range(101):
        for j in range(101):
            check_x = (
                machine.get_button_a_X() * i + machine.get_button_b_X() * j
            )

            if check_x != machine.get_prize_X():
                continue

            check_y = (
                machine.get_button_a_Y() * i + machine.get_button_b_Y() * j
            )
            if check_y == machine.get_prize_Y():
                return 3 * i + j

    return 0  # No prize


def calculate_total_tokens(machines: List[Machine]) -> int:
    total_tokens = 0
    for machine in machines:
        total_tokens += calculate_tokens(machine)
    return total_tokens


# -------------------------------------------------------------------------------

machines: List[Machine] = read_file()
total_spent: int = calculate_total_tokens(machines)

print(f"Minimun tokens for winning: {total_spent}")
