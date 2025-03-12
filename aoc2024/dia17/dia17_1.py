import re
from typing import Dict, List

FILENAME = "input.txt"

with open(FILENAME) as file:
    registers_str, instructions_str = file.read().split("\n\n")

    registers: Dict[str, int] = {
        match[0]: int(match[1])
        for match in re.findall(r"Register ([A-Z]): (\d+)", registers_str)
    }
    program: List[int] = list(
        map(int, instructions_str.split(" ")[1].replace("\n", "").split(","))
    )


def instruction_0(operand: int) -> None:
    """
    Sets reg A to the value of reg A divided and truncated by 2^combo_operand
    """
    registers["A"] = registers["A"] // pow(2, get_combo_operand(operand))


def instruction_1(operand) -> None:
    """
    Sets reg B to bitwise XOR between value of reg and literal operand
    """
    registers["B"] = registers["B"] ^ operand


def instruction_2(operand: int) -> None:
    """
    Sets reg B to the value of the literal operand modulo 8.
    Only the 3 least significant bits are stored
    """
    # AND operation with 0b111 to keep only the 3 least significant bits
    registers["B"] = (get_combo_operand(operand) % 8) & 0b111


def instruction_3(operand: int):
    """
    Moves ins_pointer to operand if A is not 0
    """
    global ins_pointer
    if registers["A"] == 0:
        return False  # Does nothing if A is 0
    ins_pointer = operand
    return True


def instruction_4(operand: int) -> None:
    """
    Sets register B to the bitwise XOR between values of reg B and C
    """
    registers["B"] = registers["B"] ^ registers["C"]


def instruction_5(operand: int) -> str:
    """
    Outputs the value of the combo_operand modulo 8
    """
    return str(get_combo_operand(operand) % 8)


def instruction_6(operand: int) -> None:
    """
    Sets reg B to the value of reg A divided and truncated by 2^combo_operand
    """
    registers["B"] = registers["A"] // pow(2, get_combo_operand(operand))


def instruction_7(operand: int) -> None:
    """
    Sets reg C to the value of reg A divided and truncated by 2^combo_operand
    """
    registers["C"] = registers["A"] // pow(2, get_combo_operand(operand))


def get_combo_operand(lit_operand: int):
    if lit_operand >= 0 and lit_operand <= 3:
        return lit_operand
    if lit_operand == 4:
        return registers["A"]
    if lit_operand == 5:
        return registers["B"]
    if lit_operand == 6:
        return registers["C"]

    return float("inf")  # Invalid operand


def process_instruction(opcode: int, operand: int) -> None:
    switcher = {
        0: instruction_0,
        1: instruction_1,
        2: instruction_2,
        3: instruction_3,
        4: instruction_4,
        5: instruction_5,
        6: instruction_6,
        7: instruction_7,
    }
    func = switcher.get(opcode, lambda: "Invalid instruction")
    return func(operand)


ins_pointer = 0


def calc_ouput():
    global ins_pointer
    res = ""

    while ins_pointer < len(program):
        opcode, operand = program[ins_pointer], program[ins_pointer + 1]

        if opcode == 5:
            res += process_instruction(opcode, operand)
        elif opcode == 3:
            jumped = process_instruction(opcode, operand)
        else:
            process_instruction(opcode, operand)

        if opcode != 3 or not jumped:
            ins_pointer += 2

    return ",".join(map(str, res))


# -------------------------------------------------------------------------------

output = calc_ouput()
print(f"Output: {output}")
