from collections import defaultdict
import heapq
# remove unnececery roads

# 1. sort roads decendent从大到小
# 优先删除最贵的路

# 2 loop roads
    # if a -> b has a faster detour (*1)
        # remove road
    # else:
        # add cost


# return cost
# *1: use dijkstra to calculate the shortest paths

def minCostRoad(n, m, dic, roads):
    edge_remove = set()
    total_cost = 0
    for p1, p2, dist, cost, id in roads:
        edge_remove.add(id)
        l = dijkstra(p1,p2,edge_remove,dic)
        if l > dist:
            edge_remove.remove(id)
            total_cost += cost
    return total_cost
# [(a, 3), (a, 4), (b, 1), (b, 6)]
def dijkstra(p1, p2, edge_remove, dic):
    hp = []
    heapq.heappush(hp, (0, p1))
    visited = set()
    while hp:
        step,current= heapq.heappop(hp)
        if current in visited:
            continue 
        visited.add(current)
        if current == p2:
            return step
        for point, dist, cost, id in dic[current]:
            if point not in visited and id not in edge_remove:
                heapq.heappush(hp,(step + dist,point))
    return float('inf')
        
def take_input():
    n,m = map(int,input().split())
    roads = []
    dic = defaultdict(list)
    for i in range(m):
        p1, p2, dist, cost = list(map(int,input().split()))
        roads.append((p1, p2, dist, cost, i))
    roads.sort(key = lambda x:x[3], reverse=True)
    for i in range(m):
        p1, p2, dist, cost,id = roads[i]
        dic[p1].append([p2, dist, cost,id])
        dic[p2].append([p1, dist, cost,id])
    return n, m, dic, roads

n, m, dic, roads = take_input()
print(minCostRoad(n, m, dic, roads))