def combination_sum3(n,k):
    stack = [([],n,1)] 
    answer = []
    while stack:
        current,remain,pre= stack.pop()
 

    #1:on target:
        # 1. remain == 0
        # 2. len == k
        # 3. used once
        # append into answer
        if remain == 0 and len(current) == k:
            answer.append(current)

    #2:below target:
        # 1. remain > 0
        # 2. len < k
        # 3. didn't use
        
        # add number
        elif remain > 0 and len(current) < k:
            for i in range(pre,10):
                stack.append((current + [i],remain - i, i + 1))       

    #3:over target:
        # 1. remain < 0
        # or
        # 2. len == k
        
        #continue
    return answer
        