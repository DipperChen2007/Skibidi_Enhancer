graph1 = {
    'a': ['b', 'c'],
    'b': ['a', 'c'],
    'c': ['a']
}

# use graph to find target, if found, return True, return False otherwise
def dfs(graph, target):
    stack = ['a']
    visited = set()
    while stack:
        current = stack.pop()
        # check if visited
        if current in visited:
            continue
        if current == target:
            return True
        visited.add(current)
        # expand
        for point in graph[current]:
            if point not in visited:
                stack.append(point)
                
    return False

dfs(graph1, 'c') # return True
dfs(graph1, 'd') # return False

# starting 'a', use graph to find target, if found, return the steps, return -1 otherwise
from collections import deque
def bfs(graph, target):
    queue = deque([('a',0)])
    visited = set()
    while queue:
        current,steps = queue.popleft()
        if current in visited:
            continue
        if current == target:
            return steps
        visited.add(current)
        for point in graph[current]:
            if point not in visited:
                queue.append((point,steps+1))
    
    return -1

graph1 = {
    'a': [(3, 'b'), (2, 'd'), (5, 'c')],
    'b': [(3, 'a'), (1, 'c')],
    'c': [(1, 'b'), (2, 'd'), (5, 'a')],
    'd': [(2, 'a'), (2, 'c')]
}
# MST 于BFS, DFS之间最大的区别在于每一个edge都带有一个weight(长度)，我们需要根据长度来决定使用哪条边
# starting from 'a', find the minimum total length to connect the entire graph
# 从a点出发， 拓展相邻的点和线，放在heap里面，按照长度排序

# heap不同于stack和queue，放进去的东西永远会按照从小到大的顺序排列好，insert的速度是O(n^2)
# heappop会取出里面的第0个element，所以heap永远会取出最小的

# init heap[(0, 'a')]
# expand a: heap[(2, 'd'), (3, 'b'), (5, 'c')] total += 0
# expand d: heap[(2, 'a'), (2, 'c'), (3, 'b'), (5, 'c')] total += 2
# expand a: heap[(2, 'c'), (3, 'b'), (5, 'c')] a visited
# expand c: heap[(1, 'b'), (2, 'd'), (3, 'b'), (5, 'c'), (5, 'a')] total += 2
# expand b: heap[(1, 'c'), (2, 'd'), (3, 'b'), (3, 'a'), (5, 'c'), (5, 'a')] total += 1
# expand c: heap[]
import heapq
def MST(graph):
    hp = []
    heapq.heappush(hp,(0,'a'))
    visited = set()
    graph_total = 0
    while hp:
        length, current = heapq.heappop(hp)
        if current in visited:
            continue
        # 查完立马放
        visited.add(current)
        graph_total += length
        for (l,point) in graph[current]:
            if point not in visited:
                heapq.heappush(hp,(l,point))
    return graph_total
    
# find the shortest path from start to end, return the minimum length
def djisktra(graph, start, end):
    pass