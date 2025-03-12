from collections import defaultdict
from typing import Dict, List, Tuple

FILENAME = "input.txt"
PRICE_CHANGES = 2000


def next_secret_number(sec_n: int) -> int:
    sec_n = (sec_n ^ (sec_n << 6)) & 0xFFFFFF
    sec_n = (sec_n ^ (sec_n >> 5)) & 0xFFFFFF
    sec_n = (sec_n ^ (sec_n << 11)) & 0xFFFFFF
    return sec_n


def get_most_bananas(
    buyers_diffs: List[List[int]], buyers_bananas: List[List[int]]
) -> int:
    bananas: Dict[Tuple[int], int] = defaultdict(
        int
    )  # Store the bananas for each sequence

    for n, _ in enumerate(buyers_diffs):
        # Only want the first appear of a sequence so
        # For each buyer, we store the sequences we have seen
        seen_seqs = set()

        for i in range(PRICE_CHANGES - 3):
            seq = tuple(buyers_diffs[n][i : i + 4])

            if seq not in seen_seqs:
                bananas[seq] += buyers_bananas[n][i + 3]
                seen_seqs.add(seq)

    return max(bananas.values())


# -------------------------------------------------------------------------------
secret_nums: List[int] = [int(num) for num in open(FILENAME)]
buyers_diffs: List[List[int]] = []  # List of differences for each buyer
buyers_bananas: List[List[int]] = []  # List of bananas for each buyer

for num in secret_nums:
    diffs = []
    bananas = []

    for _ in range(PRICE_CHANGES):
        prev = num
        num = next_secret_number(num)
        diffs.append((num % 10) - (prev % 10))
        bananas.append(num % 10)

    buyers_diffs.append(diffs)
    buyers_bananas.append(bananas)

res = get_most_bananas(buyers_diffs, buyers_bananas)
print(f"The most bananas I can get is: {res}")

