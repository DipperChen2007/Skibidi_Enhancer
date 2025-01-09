from collections import defaultdict

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
        for t in zone[i]:
            for j in range(i + 1,n + 1):
                if t in zone[j]:
                    zone_connection[i].append((j,t))
                    zone_connection[j].append((i,t))
    return zone,zone_connection

zone,zone_connection = take_input()
print(zone,zone_connection)