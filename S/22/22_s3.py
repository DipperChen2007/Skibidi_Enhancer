def Good_Samples(n,m,k):
    # You have been instructed to make a piece of music with exactly N notes
    # they will not play any note with pitch higher than M
    
    # return -1
    # max_sample = 0
    # for i in range(n):
    #     # i => 0, 1, 2, 3, 4, 5, 6, 7, ...
    #     # m => m = 5 => 1, 2, 3, 4 => m - 1 == 4
    #     max_sample += min(i+1, m)

    # if k > max_sample:
    #     print(-1)
    #     return 
    
    # retuan sample
    # they want a piece with exactly K good samples
    answer_lst = []
    remaining_samples = k
    for i in range(n):
        remaining_slot = n - (i + 1)
        back_find = min(m, remaining_samples - remaining_slot)

        if back_find <= 0:
            break

        # if back_find is out of range, use pitch to add new number
        pitch = 0
        if back_find > i:
            pitch = i + 1
            back_find = pitch
        else:
            pitch = answer_lst[i - back_find]
        
        remaining_samples -= back_find
        answer_lst.append(pitch)

    
    if remaining_samples == 0 and len(answer_lst) == n:
        return " ".join(map(lambda x: str(x), answer_lst))
    
    return -1

def take_input():
    n,m,k = list(map(int,input().split()))
    return n,m,k

n,m,k = take_input()
print(Good_Samples(n,m,k))

def goodSample(N, M, K):
    ans = []

    for i in range(N):
        rem = N - (i + 1)
        currSample = min(K - rem, M)

        if currSample <= 0:
            break

        val = 0
        if currSample > i:
            val = i+1
            currSample = val
        else:
            val = ans[i - currSample]
        
        K -= currSample
        ans.append(val)
    
    if K == 0 and len(ans) == N:
        return " ".join(map(lambda x: str(x), ans))
    
    return -1

N, M, K = map(lambda x: int(x), input().split())
print(goodSample(N, M, K))