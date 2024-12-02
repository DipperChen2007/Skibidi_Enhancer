from collections import defaultdict
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
def MST(n,m,lst):
    edges = 0
    parent = []
    rank = []
    for i in range(m):
        rank.append(0)
        parent.append(i)
    result = []
    i = 0
    total_edges = n 
    
    while edges < total_edges:
        p1,p2,l,c = lst[i]
        i += 1
        pass


def find_parent(parent,child):
    if parent[child] != child:
        parent[child] = find_parent(parent,parent[child])
    return parent[child]
    
        

def take_input():
    n,m = map(int,input().split())
    lst = []
    for _ in range(m):
        lst.append(list(map(int,input().split())))
    lst.sort(key = lambda x:x[3])
    return n,m,lst

n,m,lst = take_input()
print(n,m,lst)