#https://leetcode.ca/all/253.html
from collections import deque
def Meeting_rooms(lst):
    lst.sort(key = lambda x:x[1])
    frontier = deque([])
    answer = 0
    for start,end in lst:
        frontier.append((start,end))
        while start >= frontier[0][1]:
            frontier.popleft()
        answer = max(len(frontier),answer)   
    return answer

lst = [[7,10],[2,4]]
print(Meeting_rooms(lst))               