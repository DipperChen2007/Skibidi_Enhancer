from collections import Counter
from collections import defaultdict
def Absolutely_Acidic(lst):

    # [1 1 1 10 10 10 2 2 3 3]
    # {1: 3, 10: 3, 2: 2, 3: 2}
    count = Counter(lst)
    freqToNumbers = defaultdict(list)
    for key, val in count.items():
        freqToNumbers[val].append(key)
        
    # {3: [1, 10], 2: [2, 3]}
    # 对freqToNumbers按frequency进行sort，找出最大和第二大freq
    sort_freq = (sorted(freqToNumbers.items(), key=lambda item: item[0],reverse = True))
    # [(3, [1, 10]), (2, [2, 3])]
    # 1 1 1 10 10 10
    # 找出最高频和第二高频的数字
    leng_1 = len(sort_freq[0][1])
    

    # 1. 第一高频 x 2 +
        # 从第一高频种找出差值最大的数字
        # [1, 2, 3, 4, 5]
    if len(sort_freq) == 1 or leng_1 >= 2:
        return max(sort_freq[0][1]) - min(sort_freq[0][1])
    else:
        leng_2 = len(sort_freq[1][1])
        # 2. 第一高频 x 1，第二高频 x 1
            # 直接得出答案
        if leng_1 == 1 and leng_2 == 1:
            return abs(sort_freq[0][1][0] - sort_freq[1][1][0])
            
        # 3. 第一高频 x 1，第二高频 x 2 +
            # 从第二高频种找出和第一高频差值最大的数字
            # [10] [1, 3, 5]
        else:
            answer = 0
            for number in sort_freq[1][1]:
                answer = max(answer,abs(sort_freq[0][1][0] - number))
            return answer
        
def Take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    return lst

lst = Take_input()
print(Absolutely_Acidic(lst))