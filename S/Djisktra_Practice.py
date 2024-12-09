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


def djisktra(graph):
    pass