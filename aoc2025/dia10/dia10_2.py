import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum

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
        new_button = np.array([int(x) for x in "".join(new_button)])
        button_list.append(new_button)

    joltage_req = parts[-1]
    joltage_req = joltage_req.replace("{", "")
    joltage_req = joltage_req.replace("}", "")
    joltage_req = joltage_req.split(",")
    joltage_req = np.array([int(x) for x in joltage_req])

    machines.append(
        {
            "light_d": light_d,
            "buttons": button_list,
            "joltage_req": joltage_req,
        }
    )


def count_pushes(machine):
    _, buttons, joltage_req = machine.values()

    A_eq = np.array(buttons).T
    num_eqs, buttons_len = A_eq.shape

    modelo = LpProblem("Min pushes", LpMinimize)

    x = [
        LpVariable(f"x_{i}", lowBound=0, cat="Integer")
        for i in range(buttons_len)
    ]
    modelo += lpSum(x), "Objective"

    for i in range(num_eqs):
        restriccion_i = np.dot(A_eq[i, :], x)
        modelo += restriccion_i == joltage_req[i], f"Restriction_{i + 1}"

    modelo.solve()

    return modelo.objective.value()


print(int(sum(count_pushes(machine) for machine in machines)))
