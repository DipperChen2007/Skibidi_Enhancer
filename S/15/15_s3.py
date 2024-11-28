def gates(numbers_of_gates,planes):
    gate_state = [0] * numbers_of_gates
    landed = 0
    for plane in planes:
        gate = plane - 1
        
        while gate >= 0 and gate_state[gate] != 0:
            previous_gate = gate
            gate -= gate_state[gate]
            gate_state[previous_gate] += 1
        
        if gate < 0:
            return landed 
        else:
            landed += 1
            gate_state[gate] += 1  
            
    return landed 
  
            
def Take_input():
    numbers_of_gates = int(input())
    numbers_of_planes = int(input())
    lst = []
    for _ in range(numbers_of_planes):
        lst.append(int(input()))

    return numbers_of_gates,lst

numbers_of_gates,lst = Take_input()
print(gates(numbers_of_gates,lst))