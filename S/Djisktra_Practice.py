graph1 = {
    'a': ['b', 'c'],
    'b': ['a'],
    'c': ['a']
}

# use graph to find target, if found, return True, return False otherwise
def dfs(graph, target):
    frontier = ['a']
    visited = set()
    while frontier:
        current = frontier.pop()
        # check if visited
        if current in visited:
            continue
        visited.add(current)
        # expand
        for point in graph[current]:
            if point not in visited:
                frontier.append(point)
                
    if target in visited:
        return True
    else:
        return False


dfs(graph1, 'c') # return True
dfs(graph1, 'd') # return False

def djisktra(graph):
    pass