from collections import defaultdict
import heapq
# graph_input= [[1,   7,   6],
#             [2,    8,    2],
#             [2,    6,    5],
#             [4,    0,   1],
#             [4,    2,    5],
#             [6,    8,    6],
#             [7,    2,    3],
#             [7,    7,    8],
#             [8,    0,    7],
#             [8,    1,    2],
#             [9,    3,    4],
#             [10,    5,    4],
#             [11,    1,    7],
#             [14,    3,    5]]

graph_input = [[0, 1, 10],
            [0, 2, 6],
            [3, 0, 5],
            [1, 3, 15],
            [3, 2, 4]]

def MST(graph):
    graph.sort(key=lambda x:x[2])
    e = 0
    parent = []
    rank = []
    for i in range(len(graph.keys())):
        rank.append(0)
        #[0,0,1,0]
        parent.append(i)
        #[0,2,2,3]
   
    result = []
    i = 0 
    total_edges = len(graph.keys()) - 1
    
    while e < total_edges:
        u,v,w = graph[i]
        i += 1
        u_parent = Find_parent(parent,u)
        v_parent = Find_parent(parent,v)
        if u_parent != v_parent:
            e+=1
            result.append(w)
            Update_parent(parent,u,v,rank)

    return sum(result)
    
     
def Find_parent(parent,child):
    if parent[child] != child:
        parent[child] = Find_parent(parent,parent[child])
    return parent[child]


def Update_parent(parent,u,v,rank):
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u 
    else:
        parent[u] = v
        rank[u] += 1
        rank[v] = rank[u]
    
    
def Take_input():
    
    graph = defaultdict(list)
    for line in graph_input:
        point_1,point_2,weight = line[0],line[1],line[2]
        graph[point_1].append((point_2,weight))
        graph[point_2].append((point_1,weight))
        
    return graph    


def minCostConnectPoints(points):
    graph = defaultdict(list)
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x1,y1 = points[i]
            x2,y2 = points[j]
            distance = abs(x1-x2) + abs(y1-y2)
            graph[i].append([j,distance])
            graph[j].append([i,distance])
    visited = set()
    result = 0
    min_heap = [[0,0]]
    while len(visited) < len(points):
        cost,point = heapq.heappop(min_heap)
        if point in visited:
            continue
            
        result += cost
        visited.add(point)

        for neighbour,distance in graph[point]:
           if neighbour not in visited:
                heapq.heappush(min_heap,[distance,neighbour])
    return result
