def Sum_Game(n,team_1,team_2):
    dp = [0]*(n + 1)
    sum_1 = 0
    sum_2 = 0
    dp[0] = 1
    for i in range(n):
        sum_1 += team_1[i]
        sum_2 += team_2[i]
        if sum_1 == sum_2:
            dp[i+1] += 1
    answer = 0
    for j in range(n + 1):
        if dp[j] == 1:
            answer = max(answer,j)
    return answer            
        
def take_input():
    n = int(input())
    team_1 = list(map(int,input().split()))
    team_2 = list(map(int,input().split()))
    return n,team_1,team_2

n,team_1,team_2 = take_input()
print(Sum_Game(n,team_1,team_2))