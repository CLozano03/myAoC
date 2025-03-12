from typing import List

FILENAME = "input.txt"


def read_file() -> List[int]:
    with open(FILENAME, "r") as file:
        return [int(d) for d in file.readline().strip()]


# -------------------------------------------------------------------------------


def uncompress_disk(disk: List[int]) -> List[int]:
    files = []
    is_file = False
    n_file = 0

    for num_blocks in disk:
        is_file = not is_file  # Alternates between File and Free Space
        for _ in range(num_blocks):
            if is_file:
                files.append(n_file)  # Indicates the position of the file
            else:
                files.append(-1)

        if is_file:
            n_file += 1

    return files


def disk_info(disk: List[int], files_or_free: bool) -> List[int]:
    ret = []
    start = 0 if files_or_free else 1

    for i in range(start, len(disk), 2):
        if disk[i] == 0:
            continue

        ret.append(disk[i])

    return ret


# Returns a list of starting positions of each file
def pos_info(disk: List[int], files_or_free: bool) -> List[int]:
    pos = []
    pos_accum = 0

    for i in range(0, len(disk)):
        if disk[i] == 0:
            continue

        if files_or_free:
            if i % 2 == 0:
                pos.append(pos_accum)
        else:
            if i % 2 == 1:
                pos.append(pos_accum)

        pos_accum += disk[i]

    return pos


def move_file_entirely(
    files: List[int], from_pos: int, to_pos: int, num_blocks: int
) -> List[int]:
    files_new = files.copy()

    for i in range(num_blocks):
        files_new[to_pos + i] = files[from_pos + i]
        files_new[from_pos + i] = -1  # Mark old position as free

    return files_new


def compact_disk(disk: List[int]) -> List[int]:
    uncompressed_disk = uncompress_disk(disk)
    compacted_disk = uncompressed_disk.copy()

    file_sizes = disk_info(disk, files_or_free=True)
    pos_info_files = pos_info(disk, files_or_free=True)

    # Iterate over files in reverse order (highest file ID first)
    for file_index in range(len(file_sizes) - 1, -1, -1):
        file_size = file_sizes[file_index]
        file_start = pos_info_files[file_index]

        # Find the leftmost span of free space that can fit the file
        free_start = -1
        free_length = 0

        for i in range(len(compacted_disk)):
            if i >= file_start:
                break  # No need to check beyond the file's starting position

            if compacted_disk[i] == -1:
                if free_start == -1:
                    free_start = i
                free_length += 1

                if free_length >= file_size:
                    compacted_disk = move_file_entirely(
                        compacted_disk, file_start, free_start, file_size
                    )
                    break
            else:
                free_start = -1
                free_length = 0

    return compacted_disk


def calculate_checksum(shorted_disk: List[int]) -> int:
    checksum = 0
    for i in range(0, len(shorted_disk)):
        if shorted_disk[i] != -1:  # Ignore -1 as they represent free space
            checksum += shorted_disk[i] * i
    return checksum


# -------------------------------------------------------------------------------

disk: List[int] = read_file()
compacted_disk = compact_disk(disk)

checksum = calculate_checksum(compacted_disk)
print(f"Filesystem checksum: {checksum}")
