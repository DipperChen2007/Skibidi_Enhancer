def M_J(r,c,cat):

    dp = [[0] * (c + 1) for _ in range(r + 1)]

    for row, col in cat:
        dp[row][col] = -1

    if dp[1][1] == -1:
        return 0
    dp[1][1] = 1
 
    for i in range(1, r + 1):
        for j in range(1, c + 1):
           
            if i == 1 and j == 1:
                continue
            
            if dp[i][j] == -1:
                continue
            ways = 0         
            if dp[i - 1][j] != -1:
                ways += dp[i - 1][j]
    
            if dp[i][j - 1] != -1:
                ways += dp[i][j - 1]
            dp[i][j] = ways
    return dp[r][c]

def take_input():
    r,c = map(int, input().split())
    num_cats = int(input())
    cat = []
    for _ in range(num_cats):
        row, col = map(int, input().split())
        cat.append((row, col))
    return r,c,cat

r,c,cat = take_input()
print(M_J(r,c,cat))
