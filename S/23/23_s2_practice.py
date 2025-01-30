def Symmetric_Mountains(n,mountains):
    dp = [[] for _ in range(n)]
    for _ in range(n):
        dp[0].append(0)
    for i in range(1,n):
        dp[1].append(abs(mountains[i]-mountains[i-1]))
    for i in range(2,n):
        for j in range(n-i):
            dp[i].append(abs(mountains[j]-mountains[j+i]) + dp[i-2][j+1])
    ans = []
    for lst in dp:
        ans.append(min(lst))
    print(*ans)

def take_input():
    n = int(input())
    mountains = list(map(int, input().split()))
    return n, mountains

n,mountains = take_input()
(Symmetric_Mountains(n,mountains))
