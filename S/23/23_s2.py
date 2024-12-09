def Symmetric_Mountains(mountains):
    answer_lst = []
    for i in range(len(mountains)):
        answer = find_symmetric(i+1,mountains)
        answer_lst.append(answer)
    print(*answer_lst)
        
def find_symmetric(i,mountains):
    answer = float('inf')
    if i == 1:
        return 0
    for j in range(len(mountains) - i + 1):
        sub_lst = mountains[j:j + i]
        abs_vlaue = 0
        for l in range(len(sub_lst)//2):
            a = abs(sub_lst[l] - sub_lst[-l - 1])
            abs_vlaue += a 
        
        answer = min(answer,abs_vlaue)
    return answer 
        

def take_input():
    n = int(input())
    mountains = list(map(int,input().split()))
    return mountains

mountains = take_input()
Symmetric_Mountains(mountains)
    