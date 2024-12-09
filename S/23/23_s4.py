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

def MST(n,m,dic):
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
        p1 = i
        for j in range(len(dic[i])):
            p2,l,c = dic[i][j]
            p1_parent = find_parent[parent,p1]
            p2_parent = find_parent[parent,p2]
            if p1_parent != p2_parent:
                e += 1
                result.append(c)
                Update_parent(parent,p1,p2,rank)
            
    return sum(result)

def Update_parent(parent,u,v,rank):
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u 
    else:
        parent[u] = v
        rank[u] += 1
        rank[v] = rank[u]
        


def find_parent(parent,child):
    if parent[child] != child:
        parent[child] = find_parent(parent,parent[child])
    return parent[child]
    
        

def take_input():
    n,m = map(int,input().split())
    lst = []
    dic = defaultdict(list)
    for _ in range(m):
        lst.append(list(map(int,input().split())))
    lst.sort(key = lambda x:x[3])
    for i in range(m):
        p1,p2,l,c = lst[i]
        dic[p1].append([p2,l,c])
        dic[p2].append([p1,l,c])
    return n,m,dic

n,m,dic = take_input()
print(MST(n,m,dic))