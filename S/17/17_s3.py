from collections import Counter
def Nailed_It(n,lst):
    times = Counter(lst)
    maximum = max(times) * 2
    numbers = list(times.keys())
    dp = [0] * (maximum + 1)
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            print(numbers[i],numbers[j]) 
            if i == j:
                dp[numbers[i] + numbers[j]] = min(times[numbers[i]],times[numbers[j]])//2
            else:               
                dp[numbers[i] + numbers[j]] = min(times[numbers[i]],times[numbers[j]])
            
    length = max(dp)
    print(dp)
    height = dp.count(length)  
    print(length,height)
                            
def Take_input():
    n = int(input())
    lst = list(map(int,input().split()))
    return n,lst

n,lst = Take_input()
(Nailed_It(n,lst))