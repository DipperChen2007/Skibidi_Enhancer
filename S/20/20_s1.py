def SSS(lst):
    answer = float('-inf')
    for i in range(len(lst) - 1):
        answer = max(answer,abs(lst[i + 1][1] - lst[i][1])/(lst[i + 1][0] - lst[i][0]))
    return answer

def take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        a,b = (list(map(int,input().split())))
        lst.append((a,b))
    lst.sort()
    return lst

lst = take_input()
print(SSS(lst))