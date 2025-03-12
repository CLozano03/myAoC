FILENAME = "input.txt"

# My program: 2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0
PROGRAM_STR = "2415751642550330"


# Simulate the program initialising register 'a' with a_init
def program(a_init: int) -> str:
    string = ""
    a, b, c = a_init, 0, 0

    while True:
        # n & 7 <-> n % 8. Because 8 is power of 2
        b = a & 7  # 2, 4
        b = b ^ 5  # 1,5
        c = a >> b  # 7, 5
        b = b ^ 6  # 1, 6
        b = b ^ c  # 4, 2
        string += str(b & 7)  # 5, 5
        a = a >> 3  # 0, 3
        if a == 0:
            break

    return string


# Realising that the program has the last number 0 and program(3) = 0
# In every iteration the program shifts the register a 3 bits to the right, the same as dividing by 8
# Or removing the last digit if the number is in octal

# So first binary digits in register a is 0b11 = 3
# a is in the form 0b11xxxxxxx...

# Conclusion: in each iteration check program output for
# a = a << 3 + nnn (nnn is number from 0 to 7)
# Only check for nnn that fits PROGRAM_STR
# If output is PROGRAM_STR then a is a solution, so print it and exit


def find_solution(curr_a: int) -> int:
    curr_a = curr_a << 3

    for n in range(curr_a, curr_a + 8):
        output: str = program(n)
        if output[0] != PROGRAM_STR[-len(output)]:
            continue

        if len(output) == len(PROGRAM_STR):
            if output == PROGRAM_STR:
                print(f"Found sol: {n}")
                exit(0)

        find_solution(n)


find_solution(3)  # Start with 3
