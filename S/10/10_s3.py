#house_length = mid
#houses = [0, 67000, 68000, 77000]
#hydrants_left = 2
#total_houses = 4

def is_possible(hose_length, houses, hydrants_left, total_houses):
    houses_left = total_houses
    is_connected = [False] * total_houses
    for i in range(total_houses):
        if is_connected[i]:
            continue
        if hydrants_left == 0 or houses_left == 0:
            break
        is_connected[i] = True
        houses_left -= 1
        hydrants_left -=1
        for j in range(i + 1,total_houses):
            distance = min((1000000 - houses[j] + houses[i]),houses[j] - houses[i]) 
            if distance <= hose_length and not is_connected[j]:
                is_connected[j] = True
                houses_left -= 1
                
    return houses_left == 0


# parameters:
# houses: position of the houses
# k: firehouse
# H: number of houses
# return: min length of a longest hose
def firehouse(houses, k, H):
    minLength = 0
    maxLength = 1000000

    while minLength < maxLength:
        mid = (minLength+maxLength) // 2
        possible = is_possible(mid * 2, houses, k, H)
        if possible:
            maxLength = mid
        else:
            minLength = mid + 1
            
    return (maxLength)

def take_input():
    h = int(input())
    houses = []
    for _ in range(h):
        houses.append(int(input()))
    houses.sort()
    k  = int(input())
    return h,k,houses


h,k,houses = take_input()    
print(firehouse(houses, k, h))