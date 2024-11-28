def Tandem_Bicycle(q,n,lst_1,lst_2):
    answer = 0
    lst_1.sort()
    if q == 1:
        lst_2.sort()
        for i in range(n):
            answer += max(lst_1[i],lst_2[i])
    else: 
        lst_2.sort()
        lst_2.reverse()
        for i in range(n):
            answer += max(lst_1[i],lst_2[i])
    return answer


def take_input():
    q = int(input())
    n = int(input())
    lst_1 = list(map(int,input().split()))
    lst_2 = list(map(int,input().split()))
    return q,n,lst_1,lst_2

q,n,lst_1,lst_2 = take_input()
print(Tandem_Bicycle(q,n,lst_1,lst_2))