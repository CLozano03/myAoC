from typing import List, Tuple
from functools import lru_cache

FILENAME = "input.txt"
BLINKING_TIMES = 75
MULTIPLY = 2024


def read_file() -> List[int]:
    with open(FILENAME, "r") as file:
        return [int(d) for d in file.readline().strip().split(" ")]


# Splits a number into two numbers of the same length (only called with even numbers)
def divide_into_to_numbers(number: int) -> Tuple[int, int]:
    half = len(str(number)) // 2
    return int(str(number)[:half]), int(str(number)[half:])


# Recursive function to calculate the amount of stones after blinking a certain amount of times a single stone
@lru_cache(
    maxsize=None
)  # Apply memoization to the function so it doesn't recalculate the same values twice
def blink_stone(stone: int, times: int) -> int:
    if times == 0:
        return 1

    if stone == 0:
        return blink_stone(1, times - 1)
    elif len(str(stone)) % 2 == 0:
        first_half, second_half = divide_into_to_numbers(stone)
        return blink_stone(first_half, times - 1) + blink_stone(
            second_half, times - 1
        )
    else:
        return blink_stone(stone * MULTIPLY, times - 1)


# Iterate through all stones and calculate the total amount of stones after blinking
def blinking(stones: List[int]) -> int:
    total_stones = 0

    for stone in stones:
        total_stones += blink_stone(stone, BLINKING_TIMES)

    return total_stones


# -------------------------------------------------------------------------------

stones = read_file()
res = blinking(stones)

print(f"Stones after blinking {BLINKING_TIMES} times: {res}")
