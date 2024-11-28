def Bridge_Transport(max_weight,lst):
    current_train = []
    current_weight = 0
    i = 0
    answer = 0
    while current_weight <= max_weight and i < len(lst):
        
        if len(current_train) == 4:
            current_weight -= current_train[0]
            current_train.pop(0)
            if current_weight + lst[i] > max_weight:
                return answer
            else:
                current_train.append(lst[i])
                current_weight += lst[i]
                i += 1
                answer += 1
        else:
            if current_weight + lst[i] > max_weight:
                return answer
            else:
                current_train.append(lst[i])
                current_weight += lst[i]
                i+=1
                answer += 1
    return answer
                
def take_input():
    max_weight = int(input())
    n_trains = int(input())
    lst = []
    for _ in range(n_trains):
        lst.append(int(input()))
    return max_weight,lst

max_weight,lst = take_input()
print(Bridge_Transport(max_weight,lst))