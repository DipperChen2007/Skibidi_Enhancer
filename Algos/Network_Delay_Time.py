#https://leetcode.com/problems/network-delay-time/description/
from collections import defaultdict 
import heapq
def NDT(times,n,k):
    dic = defaultdict(list)
    for time in times:
        dic[time[0]].append((time[1],time[2]))
    hp = []
    heapq.heappush(hp,(0,k))
    visited = set()
    time = 0
    while hp:
        step,current = heapq.heappop(hp)
        if current in visited:
            continue
        time = max(time,step)
        visited.add(current)
        for point,l in dic[current]:
            if point not in visited:
                heapq.heappush(hp,(step + l,point))    
    return -1 if len(visited) != n else time