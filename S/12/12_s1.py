from math import comb
def dont_pass(n):
    if n <= 3:
        return 0
    else:
        return comb(n - 1,3)
        
def Take_input():
    n = int(input())
    return n

n = Take_input()
print(dont_pass(n))