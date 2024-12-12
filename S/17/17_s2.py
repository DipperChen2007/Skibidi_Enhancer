def high_low_tide(n,lst):
    answer = ""
    if n%2 == 0:
        high_tide = n//2
        low_tide = high_tide - 1
    else:
        low_tide = n//2 
        high_tide = low_tide + 1
    while high_tide < n:
        answer += str(lst[low_tide]) + " " + str(lst[high_tide]) + " "
        high_tide += 1
        low_tide -= 1
    if n%2 == 1:
        answer += str(lst[0])
    return answer


def take_input():
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    return n,lst

n,lst = take_input()
print(high_low_tide(n,lst))