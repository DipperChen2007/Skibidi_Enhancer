from collections import Counter

def HLC(str_lst):
    for st in str_lst:
        st_counter = list(Counter(st).items())
        sorted_st_counter = sorted(st_counter, key = lambda x:x[1])
        s,t = sorted_st_counter[-1]
        if t == 1:
            print("F")   
        else:
            a = True
            for i in range(len(st) - 1):
                if st[i] == st[i + 1]:
                    print("F")
                    a = False
                    break
            if a == True:
                print("T")    


def take_input():
    row,col = map(int,input().split())
    str_lst = []
    for _ in range(row):
        str_lst.append(input())
    return str_lst

str_lst = take_input()
HLC(str_lst)