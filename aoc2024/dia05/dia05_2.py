from typing import List

FILENAME = "input.txt"

# Stores a number of page and the number of pages that should go after it
page_orders = {}
# List which contains all the updates stored as a List[int]
updates_list = []


def read_file():
    global page_orders, updates_list

    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()

            # Page order
            if "|" in line:
                key, value = map(int, line.split("|"))

                if key not in page_orders:
                    page_orders[key] = []
                page_orders[key].append(value)

            # Update
            elif line != "":  # Skips empty line
                update = line.split(",")
                updates_list.append(
                    list(map(int, update))
                )  # Stores it as a int list


# -------------------------------------------------------------------------------


def take_middle_of_list(l: List[int]) -> int:
    return l[(int)((len(l) - 1) / 2)]


# Checks if a List is contained in another(no order). For example: [2, 32, 11] is contained in [34, 32, 11, 2]
def contained_lists_no_order(
    big_list: List[int], small_list: List[int]
) -> bool:
    bl_copy = big_list.copy()
    for el in small_list:
        if el in bl_copy:
            bl_copy.remove(el)
        else:
            return False
    return True


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


def short_update(update):
    new_update = []  # Generating another shorted list for returning it

    # Objective: empty input list
    while update:
        # For each element, insert it dinamically into new_update if all other elements
        # are contained in the page_orders list for that element.
        for i in range(len(update)):
            page = update[i]
            if page not in page_orders:
                continue

            current_checking = update.copy()
            current_checking.remove(page)

            if contained_lists_no_order(
                big_list=page_orders[page], small_list=current_checking
            ):
                new_update.append(page)
                update.remove(page)
                break

    return new_update


def sum_pos_ordered_updates():
    total_sum = 0

    for update in updates_list:
        if not check_ordered_update(update):
            shorted_update = short_update(update)
            total_sum += take_middle_of_list(shorted_update)

    return total_sum


# -------------------------------------------------------------------------------

read_file()
res = sum_pos_ordered_updates()

print(f"Sum of middle pages of pos-correctly-ordered updates: {res}")
