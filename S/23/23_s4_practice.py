from collections import defaultdict
import heapq

def Minimum_Cost_Roads(n,m,roads,cities):
    pass


def take_input():
    n,m= map(int,input().split())
    roads = []
    for i in range(m):
        u,v,length,cost = map(int,input().split())
        roads.append((u,v,length,cost,i))
    cities = defaultdict(list)
    for u,v,length,cost,i in roads:
        cities[u].append((v,length,cost,i))
        cities[v].append((u,length,cost,i))
    return n,m,roads,cities

n,m,roads,cities = take_input()
print(cities)