from typing import List, Tuple
import sympy as sp

FILENAME = "input.txt"
PLUS_HIGHER = 10000000000000

class Machine:
    def __init__(self, button_a: Tuple[int], button_b: Tuple[int], prize: Tuple[int]):
        self.button_a: Tuple[int] = button_a
        self.button_b: Tuple[int] = button_b
        self.prize: Tuple[int] = (prize[0] + PLUS_HIGHER, prize[1] + PLUS_HIGHER)   

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

# -------------------------------------------------------------------------------   

def read_file():
    machines = []
    with open(FILENAME, 'r') as file:
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
                button_a = button_b = prize = None # Next machine

    return machines

def parse_values(line: str) -> Tuple[int]:
    parts = line.split(":")[1].split(",")
    
    if line.startswith("Prize:"):
        x_val: int = int(parts[0].strip().split("=")[1])
        y_val: int  = int(parts[1].strip().split("=")[1])
    else:
        x_val: int = int(parts[0].strip().split("+")[1])
        y_val: int = int(parts[1].strip().split("+")[1])

    return x_val, y_val

# -------------------------------------------------------------------------------   

def solve_and_check_integers(a1, b1, c1, a2, b2, c2) -> Tuple[int, int]:
    x, y = sp.symbols('x y', integer=True)  # Force integer values

    eq1 = sp.Eq(a1 * x + b1 * y, c1)
    eq2 = sp.Eq(a2 * x + b2 * y, c2)

    solutions = sp.solve([eq1, eq2], (x, y))

    if not solutions:
        return 0,0
    
    return solutions[x], solutions[y]

def calculate_total_tokens(machines: List[Machine]) -> int:
    total_tokens = 0
    for machine in machines:
        a1 = machine.get_button_a_X(); b1 = machine.get_button_b_X(); c1 = machine.get_prize_X()
        a2 = machine.get_button_a_Y(); b2 = machine.get_button_b_Y(); c2 = machine.get_prize_Y()

        x, y = solve_and_check_integers(a1, b1, c1, a2, b2, c2)
        total_tokens += 3*x + y

    return total_tokens  

# -------------------------------------------------------------------------------

machines: List[Machine] = read_file()
total_spent: int = calculate_total_tokens(machines)

print(f'Minimun tokens for winning: {total_spent}')