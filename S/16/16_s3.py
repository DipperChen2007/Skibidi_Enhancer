from collections import defaultdict

def takeInput():
    N, M = [int(i) for i in input().split()]
    phos = set(map(int, input().split()))

    graph = defaultdict(set)
    for i in range(N-1):
        u, v = [int(i) for i in input().split()]

        graph[u].add(v)
        graph[v].add(u)
    
    return N, M, phos, graph

def deleteNode(graph, node):
    for neighbor in graph[node]:
        graph[neighbor].remove(node)
    del graph[node]

# delete all the useless nodes
def cutUselessNodes(N, graph, pho):
    
    for node in range(N):
        while len(graph[node]) == 1 and node not in pho:
            prev = node
            node = list(graph[node])[0]
            deleteNode(graph, prev)

# return the length of the longest road
def findLongesetRoad(graph, phos,N):
    point = list(phos)[0]
    # find the furthest distance from a ramdom point
    furthest, start = Find_furthest_pho(graph,point,N)
    # find the furthest distance from a the previous point
    distance, end = Find_furthest_pho(graph,start,N)    
    return distance

def Find_furthest_pho(graph,point,N):
    
    distance = [-1] * N
    distance[point] = 0
    stack = [(point,-1)]
    while stack:
        current,previous = stack.pop()
        for neighbour in graph[current]:
            if neighbour != previous:
                stack.append((neighbour,current))
                distance[neighbour] = distance[current] + 1
    furthest = max(distance)
    return furthest, distance.index(furthest)
            

def calculateTotalRoads(graph):
    
    distance = 0
    for key,value in graph.items():
        distance += len(value)
        
    return distance//2
        

def phonomenalReviews(N, M, phos, graph):
    
    cutUselessNodes(N, graph, phos)
    longestLength = findLongesetRoad(graph, phos,N)
    totalLength = calculateTotalRoads(graph)
    return totalLength * 2 - longestLength

N, M, phos, graph = takeInput()
print(phonomenalReviews(N, M, phos, graph))