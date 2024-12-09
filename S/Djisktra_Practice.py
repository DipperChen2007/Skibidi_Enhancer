# for BFS
from collections import deque

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

def bfs(graph, target):


dfs(graph1, 'c') # return True
dfs(graph1, 'd') # return False

def djisktra(graph):
    pass