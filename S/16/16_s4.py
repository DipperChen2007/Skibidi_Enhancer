def Combining_Riceballs(n,lst):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    prefix_sum = [0] * (n + 1)
    
    result = max(lst)
    for i in range(n):
        dp[i][i] = lst[i]
        prefix_sum[i] = prefix_sum[i - 1] + lst[i]
        
    for interval in range(1,n):     # 区间长度
        for left_left in range(n - interval):    # 左端点
            right_right = left_left + interval
            left_right = left_left + 1
            right_left = right_right 
            while left_right <= right_left:
                left_ball = dp[left_left][left_right - 1]
                right_ball = dp[right_left][right_right]
                mid_ball = dp[left_right][right_left - 1]
                if left_ball and left_ball == right_ball and (left_right == right_left or mid_ball != 0):
                    dp[left_left][right_right] = max(dp[left_left][right_right],left_ball + right_ball + mid_ball)     
                    result = max(result,dp[left_left][right_right])              
                    break
                elif prefix_sum[left_right - 1] - prefix_sum[left_left - 1] <= prefix_sum[right_right] - prefix_sum[right_left - 1]:
                    left_right += 1
                    
                else:
                    right_left -= 1                 
    print(dp)
    print(prefix_sum)               
    return result           
                                                            
        
def Take_input():
    n = int(input())
    lst = []
    lst.extend(map(int,input().split()))
    return n,lst 

n,lst = Take_input()
print(Combining_Riceballs(n,lst))

#47 12 12 3 9 9 3