# 起始行车路线：1 4 3 2
# 行走路线：1->2, 3->4, 4->1
from collections import deque,defaultdict

def Daily_Commute(one_way_1,graph,swap,n):
    for i in range(len(swap)):
        pass

def swap(bus,point_1,point_2):
    bus[point_1],bus[point_2] = bus[point_2],bus[point_1]

def BFS(one_way_1,start,n):
    queue = deque[(start,0)]
    visited = set()
    while queue:
        current,step = queue.popleft()
        if current in visited:
            continue
        if current == n:
            return step
        visited.add(current)
        for point in one_way_1[current]:
            if point not in visited:
                queue.append((point,step + 1)) 
    return -1   
                 
def take_input():
    n,w,d = list(map(int,input().split()))
    one_way_1 = defaultdict(list)
    for _ in range(w):
        a,b = list(map(int,input().split()))
        one_way_1[a].append(b)
        
    walk = {}
    for i in range(n):
        walk[i + 1] = BFS(one_way_1,i + 1,n)

    graph = list(map(int,input().split()))
    swap = []
    for i in range(d):
        swap.append(list(map(int,input().split())))
    # 1 4 3 2
    bus = {}
    for i in range(n):
        bus[graph[i]] = i
        
    return walk,bus,swap,n 

{
    1: 0,
    2: 3,
    3: 1,
    4: 2
}

{
    1: -1,
    2: -1,
    3: 1,
    4: 0
}

{
    1: -1,
    2: -1,
    3: 3,
    4: 1
}
# calculate before first swap
getOffStation = 4
minTravelTime = 1

timeA = calcMinTavelTime(swapA, bus, walk)
timeB = calcMinTavelTime(swapB, bus, walk)

if getOffStation == swapA or getOffStation == swapB:
    if timeA < timeB:
        getOffStation = swapA
        minTravelTime = timeA
    else:
        getOffStation = swapB
        minTravelTime = timeB
else:
    # compare swapA, swapB and getOffStation
    pass