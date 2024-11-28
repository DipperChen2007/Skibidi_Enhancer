def Voronoi_Villages(lst):
    answer = float('inf')
    for i in range(1,len(lst) - 1):
        l = (lst[i] - lst[i - 1])/2
        r = (lst[i + 1] - lst[i])/2
        if (l + r) < answer:
            answer  = l+r
    return answer

def Take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort()
    return lst

lst = Take_input()
print(Voronoi_Villages(lst))