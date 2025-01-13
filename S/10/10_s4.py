from collections import defaultdict
import heapq

 #{1: [(2, 7), (4, 4)], 2: [(1, 7), (4, 7), (3, 2)], 4: [(1, 4), (2, 7), (3, 4)], 3: [(2, 2), (4, 4)]})

def Animal_Farm(zone_connection):
        hp = []
        heapq.heappush(hp,(0,1))  # (zone, code)
        visited_zone = set()
        graph_total = 0
        while hp:
            if len(visited_zone) == len(zone_connection) - 1 and len(zone_connection) not in visited_zone:
                return graph_total
            value,zone = heapq.heappop(hp)
            if zone in visited_zone:
                continue
            # 查完立马放
            visited_zone.add(zone)
            graph_total += value               
            for (z,v) in zone_connection[zone]:
                if z not in visited_zone:
                    heapq.heappush(hp,(v,z))
        return graph_total

def take_input():
    n= int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    #[[3 1 2 3 7 4 6]
    #[4 1 2 4 5 7 7 2 6]
    #[4 4 7 6 5 4 8 9 2]
    #[5 3 2 4 7 8 4 7 4 7 7]]
    zone = defaultdict(list)
    for i in range(n):
        for j in range(lst[i][0] - 1):
            first_p = lst[i][1 + j]
            second_p = lst[i][1 + j + 1]
            value =  lst[i][1 + j + lst[i][0]]
            if first_p > second_p:
                zone[i+1].append((second_p,first_p,value))
            else:
                zone[i+1].append((first_p,second_p,value))
        zone[i+1].append((lst[i][1],lst[i][lst[i][0]],lst[i][-1]))
    zone_connection = defaultdict(list)
    for i in range(1,n + 1):
        for p1,p2,v in zone[i]:
            twoZones = False
            for j in range(i + 1,n + 1):
                if (p1,p2,v) in zone[j]:
                    zone_connection[i].append((j,v))
                    zone_connection[j].append((i,v))
                    twoZones = True
            if not twoZones:
                zone_connection[i].append((n + 1,v))
                zone_connection[n + 1].append((i,v))
                
    return zone_connection

zone_connection = take_input()
print(Animal_Farm(zone_connection))










# answer


inside_edges = []
edge_to_pen = {}

num_pens = int(input())
for pen_idx in range(num_pens):
    data = [int(data) for data in input().split()]

    num_edges = data[0]
    corners = data[1: num_edges + 1]
    edges = [tuple(sorted([corners[idx], corners[(idx + 1) % num_edges]]))
             for idx in range(num_edges)]
    edge_costs = data[num_edges + 1:]

    for idx in range(num_edges):
        if edges[idx] in edge_to_pen:
            other_pen_idx, _ = edge_to_pen.pop(edges[idx])
            inside_edges.append((edge_costs[idx], pen_idx, other_pen_idx))
        else:
            edge_to_pen[edges[idx]] = (pen_idx, edge_costs[idx])

outside_edges = []
outside_idx = num_pens
for pen_idx, cost in edge_to_pen.values():
    outside_edges.append((cost, pen_idx, outside_idx))

def kruskal(edges, n):
    edges.sort()

    parents = [edge for edge in range(n)]
    def find(x):
        while x != parents[x]:
            x = parents[x]
        return x

    total_cost = 0
    for cost, x, y in edges:
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            total_cost += cost
            parents[x_root] = y_root

    return total_cost

print(min(kruskal(inside_edges, num_pens),
          kruskal(inside_edges + outside_edges, num_pens + 1)))