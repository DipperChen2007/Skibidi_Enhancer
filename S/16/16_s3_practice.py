from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def dfs(start, graph, N):
    dist = [-1] * N
    dist[start] = 0

    stack = [(start, -1)]
    while stack:
        cur, prev = stack.pop()
        for adj in graph[cur]:
            if adj != prev:
                stack.append((adj, cur))
                dist[adj] = dist[cur] + 1
    far = max(dist)
    return far, dist.index(far)
    
    
def pruning(N, graph, pho):
    for node in range(N):
        while len(graph[node]) == 1 and node not in pho:
            prev = node
            node = list(graph[node])[0]
            graph[prev].remove(node)
            graph[node].remove(prev)
            
def take_input():
    input = sys.stdin.readline
    n,m = map(int,input().split())
    phos = list(map(int,input().split()))
    dic = defaultdict(list)
    for _ in range(n - 1):
        a,b = map(int,input().split())
        dic[a].append(b)
        dic[b].append(a)
    return n,phos,dic

n,phos,dic = take_input()
pruning(n, dic, phos)
d,node = dfs(phos[0],dic,n)
d,node = dfs(node,dic,n)
two_n = 0
for key,value in dic.items():
    two_n += len(value)
print(two_n - d)