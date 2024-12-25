from typing import List

FILENAME = "input.txt"

def append_lock_key(matrix: List[List[str]]) -> None:
    '''
    Generating a List[int] with number of pins in each column of the lock or key.
    Appending the List[int] to locks or keys.
    '''
    lock_key_l: List[int] = [0, 0, 0 ,0, 0]
    
    for i in range(1, len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row)):
            if matrix[i][j] == "#":
                lock_key_l[j] += 1        
        
    if matrix[0][0] == "#":
        locks.append(lock_key_l)
    else:
        keys.append(lock_key_l)

def fit_lock_key(lock: List[int], key: List[int]) -> bool:
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True 

def locks_keys_that_fit() -> int:
    count = 0

    for lock in locks:
        for key in keys:
            if fit_lock_key(lock, key):
                count += 1
    return count

# -------------------------------------------------------------------------------
locks: List[List[int]] = []
keys: List[List[int]] = []

for line in open(FILENAME).read().split("\n\n"):
    matrix = [list(row) for row in line.split("\n")]
    append_lock_key(matrix)

print(f'Number of locks that fit with keys: {locks_keys_that_fit()}')