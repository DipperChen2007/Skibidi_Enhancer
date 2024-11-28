def lunch_concert(left,right,friends):
    while left < right:
        mid = (left + right)//2
        mid_time = toutoutime(friends,mid)
        left_time = toutoutime(friends,mid - 1)
        right_time = toutoutime(friends,mid + 1)
        if left_time > mid_time and mid_time > right_time:
            left = mid + 1
        elif left_time < mid_time and mid_time < right_time:
            right = mid - 1
        else:
            return mid_time
    left_time = toutoutime(friends, left)
    return left_time

#check
def yigexiaoren(friend,c):
    pos,w,d = friend
    distance = abs(c - pos)
    if distance <= d:
        return 0
    return (distance - d) * w

#check
def toutoutime(friends,c):
    time = 0
    for friend in friends:
        time += yigexiaoren(friend,c)
    return time

def Take_input():
    n = int(input())
    friends = []
    left = float('inf')
    right = float('-inf')
    for _ in range(n):
        pos,w,d = [int(i) for i in input().split()]
        left = min(pos,left)
        right = max(pos,right)
        friends.append([pos,w,d])
    
    return left,right,friends

left,right,friends = Take_input()
print(lunch_concert(left,right,friends))