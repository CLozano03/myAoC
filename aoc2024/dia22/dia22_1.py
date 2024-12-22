from typing import List

# 16777216 = 2^24 # 1 0000 0000 0000 0000 0000 0000
# PRUNE(a) = a & 0xFFFFFF  # a & 1111 1111 1111 1111 1111 1111
# MIX(a, b) = a ^ b

FILENAME = "input.txt"
    
def next_secret_number(sec_n: int) -> int:
    sec_n = (sec_n ^ (sec_n << 6)) & 0xFFFFFF
    sec_n = (sec_n ^ (sec_n >> 5)) & 0xFFFFFF
    sec_n = (sec_n ^ (sec_n << 11)) & 0xFFFFFF
    return sec_n

# -------------------------------------------------------------------------------
secret_nums: List[int] = [int(num) for num in open(FILENAME)]
res: int = 0

for num in secret_nums: 
    for _ in range(2000):
        num = next_secret_number(num)
    res += num # After 2000 iterations add the number to the result
    
print(f'The sum of the 2000th secret numbers is: {res}')