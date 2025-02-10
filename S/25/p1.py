def Questionnaire(lst,m):
    return_lst = []
    for i in range(len(lst)):
        return_lst.append((i,lst[i]))

    sorted_return_lst = sorted(return_lst,key = lambda x:x[1])[::-1]
    lst_1 = [0]*m
    for j in range(len(sorted_return_lst)):
        pos,amount = sorted_return_lst[j]
        lst_1[pos] = j + 1
    
    print(sorted_return_lst)
    print(lst_1)
    
def take_input():
    n,m = map(int,input().split())
    lst = [0] * m
    for _ in range(n):
        numbers = list(map(int,input().split()))
        for i in range(len(numbers)):
            lst[i] += numbers[i]
    return lst,m

lst,m = take_input()
Questionnaire(lst,m)