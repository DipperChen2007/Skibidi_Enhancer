def combination_sum(arr,target):
    arr.sort()
    frontier = [([],target)]
    answer = []
    while frontier:
        current,remain = frontier.pop()
        if remain == 0:
            answer.append(current)
        for i in arr:
            if not current and (remain - i >= 0):
                frontier.append((current + [i],remain - i))
            elif(remain - i >= 0) and i >= current[-1]:            
                frontier.append((current + [i],remain - i))
    return answer
print(combination_sum([2,3,6,7],7))