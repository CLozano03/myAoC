with open("input.txt") as f:
    lines = f.read().splitlines()

rack = {}

for line in lines:
    device, outputs = line.split(":")
    rack[device] = outputs.split()


def count_out(dev):
    if dev not in rack:
        return 0
    outputs = rack[dev]
    count = 0

    if "out" in outputs:
        count += 1

    for out in outputs:
        count += count_out(out)

    return count


outs = count_out("you")
print(outs)
