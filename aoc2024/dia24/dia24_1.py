from typing import Dict, Tuple, List

FILENAME = "input.txt"
Z_REGS = {f"z{n:02}" for n in range(0, 46)} # Set of all z registers (looking at the input)

# -------------------------------------------------------------------------------
regs: Dict[str, int] = {}
gates: List[Tuple[str, str, str, str]] = []

with open(FILENAME) as f:
    p1, p2 = f.read().split("\n\n")
    
    # Reading registers
    for reg in p1.split("\n"):
        reg, val = reg.split(": ")
        regs[reg] = int(val)
        
    # Reading gates
    for op in p2.split("\n"):
        tuple_op = op.split(); tuple_op.remove("->")
        gates.append(tuple_op)

while not Z_REGS <= regs.keys():
    
    for op in gates:
        in1, op, in2, write = op

        if in1 not in regs.keys() or in2 not in regs.keys(): continue
        if op == "AND":
            regs[write] = regs[in1] & regs[in2]
        elif op == "OR":
            regs[write] = regs[in1] | regs[in2]
        elif op == "XOR":
            regs[write] = regs[in1] ^ regs[in2]
    
res_str = ""   
for reg in sorted(list(Z_REGS)):
    res_str += f"{regs[reg]}"
    
print(int(res_str[::-1], 2))
