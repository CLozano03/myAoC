from typing import List

FILENAME = "input.txt"


def check_safe(report: List[int]) -> bool:
    safe = True
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff == 0:
            return False

        # First iteration, select incr or decr
        if i == 1 and diff > 0:
            incr = True
        if i == 1 and diff < 0:
            incr = False

        if incr:
            if diff < 1 or diff > 3:
                safe = False
                break
        else:
            if diff > -1 or diff < -3:
                safe = False
                break

    return safe


def read_file():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        return lines


def sum_safe_reports(reports):
    safe_reports_sum = 0

    for line in reports:
        report = list(map(int, line.split()))

        if check_safe(report):
            safe_reports_sum += 1
            continue

    return safe_reports_sum


# -------------------------------------------------------------------------------

lines = read_file()
res = sum_safe_reports(lines)

print(f"Num of safe reports : {res}")
