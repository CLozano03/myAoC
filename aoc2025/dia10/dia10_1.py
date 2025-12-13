from itertools import combinations

with open("input.txt") as f:
    lines = f.read().splitlines()

machines = []
for line in lines:
    parts = line.split()
    light_d = parts[0]
    light_d = light_d.replace("[", "")
    light_d = light_d.replace("]", "")
    light_d = light_d.translate(str.maketrans({"#": "1", ".": "0"}))
    lightlength = len(light_d)

    buttons = parts[1:-1]
    button_list = []
    for button in buttons:
        button = button.replace("(", "")
        button = button.replace(")", "")
        button = button.split(",")
        new_button = list("0" * lightlength)

        for index in button:
            new_button[int(index)] = "1"
        button_list.append("".join(new_button))

    joltage_req = parts[-1]
    joltage_req = joltage_req.replace("{", "")
    joltage_req = joltage_req.replace("}", "")
    joltage_req = joltage_req.split(",")

    machines.append(
        {
            "light_d": light_d,
            "buttons": button_list,
            "joltage_req": joltage_req,
        }
    )

count = 0


def count_pushes(machine):
    light_d, buttons, _ = machine.values()

    light_d = int(light_d, 2)

    for k in range(1, len(buttons) + 1):
        for button_comb in combinations(buttons, k):
            result = 0
            for button in button_comb:
                result ^= int(button, 2)

            if result == light_d:
                return k

    return 0


for machine in machines:
    count += count_pushes(machine)

print(count)
