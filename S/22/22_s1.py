def g4_5(n):
    answer = 0
    for i in range(1000001):
        five = i*5
        remain = n  - five 
        if remain >= 0 and remain%4 == 0:
            answer += 1
    return answer

def take_input():
    n = int(input())
    return n 

n = take_input()
print(g4_5(n))