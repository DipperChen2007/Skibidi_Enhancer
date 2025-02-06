def A_P(dic,lst_1):
    for i in range(len(lst_1)):
        if lst_1[i] != dic[dic[lst_1[i]]] or lst_1[i] == dic[lst_1[i]]:
            return "bad"
    
    return "good"
        
def take_input():
    dic = {}
    n = int(input())
    lst_1 = list(input().split())
    lst_2 = list(input().split())
    for i in range(n):
        dic[lst_1[i]] = lst_2[i]
    return dic,lst_1

dic,lst_1 = take_input()
print(A_P(dic,lst_1))