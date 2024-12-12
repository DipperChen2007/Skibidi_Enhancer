def high_low(lst):
    average = sum(lst)/len(lst)
    lst_low = []
    lst_high = []
    for e in lst:
        if e < average:
            lst_low.append(e)
        else:
            lst_high.append(e)
    lst_low.sort()
    lst_high.sort()
    answer = ""
    for i in range(len(lst_low)):
        answer += str(lst_low[::-1][i])+ " " + str(lst_high[i]) + " "
    return answer 
    

def take_input():
    n = int(input())
    lst = list(map(int,input().split()))
    return lst 

lst = take_input()
print(high_low(lst))