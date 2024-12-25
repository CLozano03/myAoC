from typing import Dict, Tuple, List, Set

FILENAME = "input.txt"

XOR = 'XOR'; AND = 'AND'; OR = 'OR'

# -------------------------------------------------------------------------------
def swap_wires(_a: str, _b: str) -> None:
    inverted_gates[_a], inverted_gates[_b] = inverted_gates[_b], inverted_gates[_a]
    gates[inverted_gates[_a]], gates[inverted_gates[_b]] = gates[inverted_gates[_b]], gates[inverted_gates[_a]]

def full_adder_check_swapped() -> List[str]:
    '''
    Implementing a full adder 
    If two registers are swapped, we need to find the swapped registers
    
         x2 x1 x0
    +    y2 y1 y0
    --------------
    z... z2 z1 z0
    '''
    
    swapped: Set[str] = set()
    prev_carry = ""

    for i in range(45):
        x_in: str = f'x{i:02}'
        y_in: str = f'y{i:02}'
        z_out: str = f'z{i:02}' # Expected register to be the output of the operation
        
        sum_with_no_carry: str = gates[x_in, y_in, XOR] # Adding in binary is XOR
        carry_bit_reg: str = gates[x_in, y_in, AND] # Only carry if both bits are 1
        
        # Do we have a carry from previous operation?
        if prev_carry:
            # Find the carry bit from the previous operation
            in_reg_1, in_reg_2 = sorted([prev_carry, sum_with_no_carry])
            op = in_reg_1, in_reg_2, XOR
            
            if op not in gates: # If the operation is not in the gates, we need to swap the wires
                in_reg_1, in_reg_2 = list(set(inverted_gates[z_out][:2]) ^ set(op[:2])) # Find the two inputs that are not in the operation
                # Add to the swapping list
                swapped.add(in_reg_1)
                swapped.add(in_reg_2)
                
                # Swap the wires
                swap_wires(in_reg_1, in_reg_2)
                
            elif gates[op] != z_out: # If the operation is not the same as the expected output register, we need to swap the wires too
                # Add to the swapping list                
                swapped.add(gates[op])
                swapped.add(z_out)
                
                # Swap the wires
                swap_wires( gates[op], z_out)
                
            # Update the carry bit for next iteration
            sum_with_no_carry = gates[(x_in, y_in, XOR)] # Adding in binary is XOR
            carry_bit_reg = gates[(x_in, y_in, AND)] # Only carry if both bits are 1
            
            # prev_carry = (XOR(x_in, y_in) AND prev_carry) OR carry_bit_reg
            prev_carry = gates[*sorted([prev_carry, sum_with_no_carry]), AND] # Carry is the AND of the carry bit and the sum with no carry      
            prev_carry = gates[*sorted([prev_carry, carry_bit_reg]), OR] # Carry is the AND of the carry bit and the sum with no carry      
        else:
            prev_carry = carry_bit_reg
        
    return list(swapped)

# -------------------------------------------------------------------------------
gates: Dict[Tuple[str] ,str] = {}
inverted_gates: Dict[str, Tuple[str]] = {}

# Now we only need operations from input file
for op in open(FILENAME).read().split("\n\n")[1].splitlines():
    in1, operator, in2, _, out = op.split()
    in1, in2 = sorted([in1, in2]) # Sort the inputs so it is stored as x01, y01 instead of y01, x01
    gates[in1, in2, operator] = out
    inverted_gates[out] = in1, in2, operator

res = full_adder_check_swapped()
print(f'Swapped wires: {",".join(sorted(res))}')