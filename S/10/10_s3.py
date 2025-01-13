def is_possible(house_length, houses, hydrants_left, total_houses):
    return house_left == 0


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
        possible = is_possible(mid, houses, k, H)
        if possible:
            maxLength = mid
        else:
            minLength = mid
    retrun (maxLength)