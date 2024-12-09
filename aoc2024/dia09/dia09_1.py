from typing import List

FILENAME = "input.txt"

def read_file(): 
    with open(FILENAME, 'r') as file:
        return file.readline().strip()
        
def get_files(disk: str) -> List[int]:
    files = []
    is_file = False
    pos = 0
    
    for digit in disk:
        is_file = not is_file # Alternates between File and Free Space
        if is_file:
            num_blocks = int(digit)
            for _ in range(num_blocks):
                files.append(pos) # Indicates the position of the file
            
            pos += 1
        
    return files

def calculate_checksum(disk: str) -> int:
    files = get_files(disk)
    total_iteration, checksum = 0, 0
    is_file = False 
    
    for digit in disk:
        is_file = not is_file # Alternates between File and Free Space
        num_blocks = int(digit)
        
        # File to fill with first files
        if is_file:
            for _ in range(num_blocks):
                if not files: break
                checksum += files.pop(0) * total_iteration

                total_iteration += 1

        # Free Space to fill with last files
        else:
            for _ in range(num_blocks):
                if not files: break
                checksum += files.pop(-1) * total_iteration
                
                total_iteration += 1
        
        # Finish the loop if there are no more files
        if not files: break

    return checksum

# -------------------------------------------------------------------------------

disk = read_file()
checksum = calculate_checksum(disk)

print(f'Filesystem checksum: {checksum}')