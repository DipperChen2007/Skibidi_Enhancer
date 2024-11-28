def Combining_Riceballs(n,lst):
    dp = [[0] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = lst[i]
        
    for i in range(n):
        for j in range(i + 1,n - 2):
            if j == i + 1 and lst[i] == lst[j]:
                dp[i][j] = lst[i] + lst[j]
            elif j == i + 2 and lst[i] == lst[j]:
                dp[i][j] = lst[i] + lst[i + 1] + lst[j] 
        
    
def Take_input():
    n = int(input())
    lst = []
    lst.extend(map(int,input().split()))
    return n,lst 

n,lst = Take_input()
print(Combining_Riceballs(n,lst))