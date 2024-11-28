def Balanced_Trees(n):
    dp = {}
    dp[1] = 1
    Helper(n, dp)
    return dp[n]

def Helper(i, dp):
    if i in dp:
        return dp[i]
    total = 0
    for j in range(2,i+1):
        if i//j in dp:
            total += dp[i//j]
        else:
            total += Helper(i//j, dp)
    dp[i] = total
    return total

def Take_input():
    n = int(input())
    return n 

n = Take_input()
print(Balanced_Trees(n))