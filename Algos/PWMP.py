# https://leetcode.com/problems/path-with-maximum-probability/description/
from collections import defaultdict
import heapq
def PWMP(n,edges,succprob,start,end):
    dic = defaultdict(list)
    for i in range(len(edges)):
        dic[edges[i][0]].append((edges[i][1],succprob[i]))
        dic[edges[i][1]].append((edges[i][0],succprob[i]))
    hp = []
    heapq.heappush(hp,(-1,start))
    visited = set()
    while hp:
        probability,current = heapq.heappop(hp)    
        if current in visited:
            continue
        if current == end:
            return abs(probability)
        for point,risk in dic[current]:
            if point not in visited:
                heapq.heappush(hp,(probability*risk,point))
    return 0
           


        
    