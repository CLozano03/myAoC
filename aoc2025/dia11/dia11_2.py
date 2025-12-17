from functools import lru_cache

with open("input.txt") as f:
    lines = f.read().splitlines()

rack = {}
for line in lines:
    device, outputs = line.split(":")
    rack[device] = outputs.split() if outputs else []


@lru_cache(None)
def dfs(dev, fft=False, dac=False):
    if dev == "out":
        return 1 if fft and dac else 0

    total_paths = 0
    for neighbor in rack[dev]:
        total_paths += dfs(
            neighbor, fft or neighbor == "fft", dac or neighbor == "dac"
        )
    return total_paths


print(dfs("svr"))
