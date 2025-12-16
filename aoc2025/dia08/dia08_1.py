import heapq

with open("input.txt") as f:
    points = [line.strip().split(",") for line in f.readlines()]


def euclidean_distance(p1, p2):
    return sum((int(x) - int(y)) ** 2 for x, y in zip(p1, p2))


circuits = []
belongs = {}
heap = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if i != j:
            dist = euclidean_distance(points[i], points[j])
            heapq.heappush(heap, (dist, i, j))


for _ in range(1000):
    if not heap:
        break

    dist, p1, p2 = heapq.heappop(heap)

    c1 = belongs.get(p1, None)
    c2 = belongs.get(p2, None)

    if c1 is not None and c2 is None:
        circuits[c1].append(p2)
        belongs[p2] = c1

    if c2 is not None and c1 is None:
        circuits[c2].append(p1)
        belongs[p1] = c2

    if c1 is None and c2 is None:
        circuits.append([p1, p2])
        idx = len(circuits) - 1
        belongs[p1] = idx
        belongs[p2] = idx

    if c1 is not None and c2 is not None and c1 != c2:
        circuits[c1].extend(circuits[c2])
        for p in circuits[c2]:
            belongs[p] = c1
        circuits[c2] = []


sizes = [len(c) for c in circuits if len(c) > 0]
sizes.sort(reverse=True)
sizes_mul = sizes[0] * sizes[1] * sizes[2]

print(sizes_mul)
