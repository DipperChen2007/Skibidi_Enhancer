def Trianglane(n,up_lst,down_lst):
    answer = 0
    for i in range(n):
        if up_lst[i] == 1:
            a = 3
            if i != n - 1:
                if up_lst[i + 1] == 1:
                    a -= 1
            
            if i != 0:
                if up_lst[i - 1] == 1:
                    a -= 1
            if i%2 != 1:
                if down_lst[i] == 1:
                    a -= 1
            answer += a
        
    for i in range(n):
        if down_lst[i] == 1:
            a = 3
            if i != n - 1:
                if down_lst[i + 1] == 1:
                    a -= 1
            
            if i != 0:
                if down_lst[i - 1] == 1:
                    a -= 1
            if i%2 != 1:
                if up_lst[i] == 1:
                    a -= 1   
                    
            answer += a
    
    return answer
            
            

def take_input():
    n = int(input())
    up_lst = list(map(int,input().split()))
    down_lst = list(map(int,input().split()))
    return n,up_lst,down_lst

n,up_lst,down_lst = take_input()
print(Trianglane(n,up_lst,down_lst))