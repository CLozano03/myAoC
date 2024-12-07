from typing import List, Tuple

FILENAME = "input.txt"

cal_values = []
num_aim = None; len_num_list = None

def read_file(): 
    with open(FILENAME, 'r') as file:
        return file.readlines()

# Returns the num_aim value if there is a possible calibration. 0 if not 
def check_calibration(curr_val: int, level=0):
    res = 0
    
    if curr_val > num_aim: return 0
    if level == len_num_list - 1:
        return num_aim if curr_val == num_aim else 0
    
    #print(f'Curr_val: {curr_val}\t\tLevel: {level}')
    
    res += check_calibration(curr_val * cal_values[level+1], level + 1)
    if res == 0: res += check_calibration(curr_val + cal_values[level+1], level + 1)
    if res == 0: res += check_calibration(int(f"{curr_val}{cal_values[level+1]}"), level + 1)
    
    return res
    
   
def calculate_calibration_res(file_lines: List[str]):
    global num_aim, cal_values, len_num_list
    
    sum_calibrated = 0
    
    for line in file_lines:
        num_part, list_part = line.split(":")
        num_aim = int(num_part.strip()) 
        cal_values = list(map(int, list_part.strip().split()))
        len_num_list = len(cal_values)
        
        print(num_aim, "  ", cal_values)
        
        sum_calibrated += check_calibration(curr_val=cal_values[0])
        print("SUM_CALIBRATED: ", sum_calibrated)
    
    return sum_calibrated

# -------------------------------------------------------------------------------

file_lines = read_file()
res = calculate_calibration_res(file_lines)

print(f'Total calibration result: {res}')