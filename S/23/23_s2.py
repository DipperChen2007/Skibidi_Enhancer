
# e.g. mount = [1,2,3,4,5]
def symMount(mount):
    # construct dp and its default value
    dp = [[] for _ in range(len(mount))]
    for i in range(len(mount)):
        # length == 1
        dp[0].append(0)
        # length == 2
        if i != len(mount)-1:
            dp[1].append(abs(mount[i]-mount[i+1]))
    
    ans = [0]

    if len(mount) >= 2:
        ans.append(min(dp[1]))

    for i in range(2, len(mount)):
        for j in range(len(mount)-i):
            # update dp[i]
            dp[i].append(abs(mount[j]-mount[j+i]) + dp[i-2][j+1])
        ans.append(min(dp[i]))
    print(*ans)
# 1 2 3 4

# [
#     [0, 0, 0, 0],
#     [1, 1, 1]
#     [2, 2]
#     [3+1]
# ]

def take_input():
    n = int(input())
    mountains = list(map(int,input().split()))
    return mountains

mountains = take_input()
symMount(mountains)
    