from collections import defaultdict
import heapq

def Convex_Hull(knm,dic,start,end):
    k,n,m = knm
    distance = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    frontier = []
    for i in range(len(distance[start])):
        distance[start][i] = 0
    heapq.heappush(frontier,(0,start,0))
    
    while frontier:
        time,island,convex =heapq.heappop(frontier) 
        if island == end:
            return time
        for dao,shij,mo in dic[island]:
            new_time = time + shij
            new_convex = convex + mo
            if  new_convex < k and new_time < distance[dao][new_convex]:
                distance[dao][new_convex] = new_time
                heapq.heappush(frontier,(new_time,dao,new_convex))
    return -1

def take_input():
    knm = list(map(int,input().split()))
    dic = defaultdict(list)
    for _ in range(knm[2]):
        a,b,c,d = list(map(int,input().split()))
        dic[a].append([b,c,d])
        dic[b].append([a,c,d])
        
    start,end = list(map(int,input().split()))
    return knm,dic,start,end

knm,dic,start,end = take_input()
print(Convex_Hull(knm,dic,start,end))