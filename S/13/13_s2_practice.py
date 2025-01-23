def Bridge_Transport(max_weight,trains):
    numbers = len(trains)
    initial = []
    current_number = 0
    current_weight = 0
    if numbers <= 4:
        for train in trains:
            initial.append(train)
            current_weight += train
            if current_weight > max_weight:
                return current_number
            current_number += 1
        return numbers
    else:
        for i in range(4):
            initial.append(trains[i])
            current_weight += trains[i]
            if current_weight > max_weight:
                return current_number
            current_number += 1
            
        for i in range(4,len(trains)):
            current_weight -= initial[0]
            initial.pop(0)
            initial.append(trains[i])
            current_weight += trains[i]
            if current_weight > max_weight:
                return current_number
            current_number += 1
    return current_number
            
        
        

def take_input():
    max_weight = int(input())
    numbers_of_trains = int(input())
    trains = []
    for _ in range(numbers_of_trains):
        trains.append(int(input()))
    return max_weight,trains

max_weight,trains = take_input()
print( Bridge_Transport(max_weight,trains))