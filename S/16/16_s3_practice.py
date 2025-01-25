from collections import defaultdict

def pruning(N, graph, pho):
    for node in range(N):
        while len(graph[node]) == 1 and node not in pho:
            prev = node
            node = list(graph[node])[0]
            graph[prev].remove(node)
            graph[node].remove(prev)
            
def take_input():
    n,m = map(int,input().split())
    phos = list(map(int,input().split()))
    dic = defaultdict(list)
    for _ in range(n - 1):
        a,b = map(int,input().split())
        dic[a].append(b)
        dic[b].append(a)
    return phos,dic

phos,dic = take_input()
