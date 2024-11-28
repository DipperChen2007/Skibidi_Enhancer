def Mouse_Journey(end,dp):
    for r in range(1,len(dp)):
        for c in range(1,len(dp[0])):
            if r == 1 and c == 1:
                dp[r][c] = 1
            elif dp[r][c] != -1:
                if dp[r - 1][c] != -1:
                    dp[r][c] += dp[r - 1][c]
                if dp[r][c - 1] != -1:
                    dp[r][c] += dp[r][c - 1]
    return dp[-1][-1]            
            
def Take_input():
    end = list(map(int,input().split()))
    dp = [[0] * (end[1] + 1) for i in range(end[0] + 1)]
    n = int(input())

    for _ in range(n):
        cat = (tuple(map(int,input().split())))
        r,c =cat
        dp[r][c] = -1
                    
    return end,dp

end,dp = Take_input()
print(Mouse_Journey(end,dp))