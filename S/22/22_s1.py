from collections import deque

def g4_5(n):
    if n == 4:
        return 1 
    elif n < 5:
        return 0
    
    visited = set()
    frontier = deque([n])
    visited.add(n)
    answer = 0
    while frontier:
        left_over = frontier.popleft()
        for i in [4,5]:
            if left_over - i == 0:
                answer += 1
                break
            elif left_over - i > 0 and (left_over - i) not in visited:
                frontier.append(left_over - i)
                print(frontier)
            else:
                break
    return answer 
    

def take_input():
    n = int(input())
    return n 

n = take_input()
print(g4_5(n))