with open("input.txt") as f:
    lines = f.read().splitlines()

ops = lines[-1]
nums = lines[:-1]
# [[123 328]
# [456 789]]

res = 0

curr_op = ""
curr_val = 0

for n in range(len(nums[0])):
    if ops[n] != " ":
        curr_op = ops[n]

    curr_num = ""
    if all(nums[i][n] == " " for i in range(len(nums))):
        res += curr_val
        curr_val = 0
        continue

    for i in range(len(nums)):
        if nums[i][n] != " ":
            curr_num += nums[i][n]

    if curr_op == "+":
        curr_val += int(curr_num)
    elif curr_op == "*":
        if curr_val == 0:
            curr_val = 1
        curr_val *= int(curr_num)

res += curr_val

print(res)
