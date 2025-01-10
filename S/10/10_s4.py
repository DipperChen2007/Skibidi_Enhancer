from collections import defaultdict
import heapq


# {
# 1: [(2, 1, 7), (4, 2, 4)], 
# 2: [(1, 1, 7), (4, 2, 7), (3, 3, 2)], 
# 4: [(1, 2, 4), (2, 2, 7), (3, 1, 4)], 
# 3: [(2, 3, 2), (4, 1, 4)]
# }

def Animal_Farm(zone_connection):
        hp = []
        heapq.heappush(hp,(1,1))  # (zone, code)
        visited = set()
        graph_total = 0
        while hp:
            zone, code = heapq.heappop(hp)
            if code in visited:
                continue
            # 查完立马放
            visited.add(code)
            for z,c,v in zone_connection[zone]:
                if c == code:
                    graph_total += v
                    
            for (z,c,v) in zone_connection[zone]:
                if c not in visited:
                    heapq.heappush(hp,(z,c))
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
        code = 1
        for p1,p2,v in zone[i]:
            for j in range(i + 1,n + 1):
                if (p1,p2,v) in zone[j]:
                    zone_connection[i].append((j,code,v))
                    zone_connection[j].append((i,code,v))
            code += 1
    return zone_connection

zone_connection = take_input()
print(zone_connection)