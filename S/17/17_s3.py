from collections import Counter
def Nailed_It(n,lst):
    times = Counter(lst)
    maximum_height = max(times) * 2
    numbers = list(set(lst))
    dp = [0] * (maximum_height + 1)
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            
            if i == j:
                dp[numbers[i] + numbers[j]] += min(times[numbers[i]],times[numbers[j]])//2
            else:               
                dp[numbers[i] + numbers[j]] += min(times[numbers[i]],times[numbers[j]])
            
    length = max(dp)
    height = dp.count(length)  
    print(length,height)

                            
def Take_input():
    n = int(input())
    lst = list(map(int,input().split()))
    return n,lst

n,lst = Take_input()
(Nailed_It(n,lst))