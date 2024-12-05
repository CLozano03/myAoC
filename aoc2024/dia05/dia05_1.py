from typing import List

FILENAME = "input.txt"

# Stores a number of page and the number of pages that should go after it
page_orders = {}
# List which contains all the updates stored as a List[int]
updates_list = []

def read_file():
    global page_orders, updates_list
    
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Page order
            if "|" in line:
                key, value = map(int, line.split("|"))
                
                if key not in page_orders:
                    page_orders[key] = []
                page_orders[key].append(value)

            # Update
            elif line != "": # Skips empty line
                update = line.split(",")
                updates_list.append(list(map(int, update))) # Stores it as a int list

# -------------------------------------------------------------------------------
 
def take_middle_of_list(l: List[int]) -> int:
    return l[(int)((len(l) - 1)/2)]

def check_ordered_update(update):
    ordered = True
    
    for i in range(len(update) - 1):
        page = update[i]
        
        if page not in page_orders:
            continue

        for aux in range(i + 1, len(update)):
            if update[aux] not in page_orders[page]:
                ordered = False
                break
            
    return ordered

def sum_correct_updates():
    total_sum = 0

    for update in updates_list:
        if check_ordered_update(update):
            total_sum += take_middle_of_list(update)
    
    return total_sum

# -------------------------------------------------------------------------------

read_file()
res = sum_correct_updates()

print(f'Sum of middle pages of correctly-ordered updates: {res}')

      
                    