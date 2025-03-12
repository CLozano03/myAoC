left = []
right_dict = {}


def read_file():
    with open("input.txt", "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())

            left.append(num1)

            if num2 in right_dict:
                right_dict[num2] += 1
            else:
                right_dict[num2] = 1


read_file()
left.sort()

sum = 0
for num in left:
    if num in right_dict:
        sum += num * right_dict[num]

print(f"Total sum of difs: {sum}")
