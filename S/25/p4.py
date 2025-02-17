from collections import defaultdict
def s_o_f(dic):
    
    
    

def take_input():
    n = int(input())
    lst = []
    dic = defaultdict(list)
    for _ in range(n):
        lst.append(list(map(int,input().split())))
        
    for i in range(len(lst)):
        a,b = lst[i]
        for j in range(i + 1,len(lst)):
            c,d = lst[j]
            if c in [a,b] or d in [a,b]:
                dic[[a,b]].append([c,d])
                
    return dic

lst = take_input()