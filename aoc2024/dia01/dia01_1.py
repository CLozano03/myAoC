left = []
right = []


def read_file():
    with open("input.txt", "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())

            left.append(num1)
            right.append(num2)


read_file()
left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(right[i] - left[i])

print(f"Total sum of difs: {sum}")
