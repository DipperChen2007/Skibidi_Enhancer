from collections import deque

def Square(n):
    answer = deque([[n]])
    visited = set()
    while [1]*n not in answer:
        lst = answer.popleft()
        if tuple(lst) in visited:
            continue
        visited.add(tuple(lst))
        if lst == [n]:
            answer.append([n-1,1])
        else:
            answer.append([[lst[0]-1]+[lst[1]+1]].sort()[::-1])      
            answer.append([[lst[0] - 1] + [lst[1:(len(lst) - 1)] + [1]]].sort()[::-1])
    for l in answer:
        print(*l)

def take_input():
    n = int(input())
    return n

n = take_input()
Square(n)