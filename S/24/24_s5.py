def M_J(r,c,cat):
    dp = [[0] * (c + 1) for i in range(r + 1)]
    dp[1][1] += 1
    for row,col in cat:
        dp[row][col] -= 1
    for i in range(1,r + 1):
        for j in range(1, c + 1):
            if dp[i][j] != -1:
                if dp[i - 1][j] != -1:
                    dp[i][j] += dp[i - 1][j]  
                if dp[i][j - 1] != -1:
                    dp[i][j] += dp[i][j - 1]
    return dp[-1][-1]
                

def take_input():
    r,c = map(int,input().split())
    cat = []
    number_or_cats = int(input())
    for _ in range(number_or_cats):
        cat.append(list(map(int,input().split())))
    return r,c,cat
r,c,cat = take_input()
print(M_J(r,c,cat))