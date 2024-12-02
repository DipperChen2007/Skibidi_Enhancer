from collections import defaultdict
# remove unnececery roads

# 1. sort roads decendent从大到小
# 优先删除最贵的路

# 2 loop roads
    # if a -> b has a faster detour (*1)
        # remove road
    # else:
        # add cost


# return cost
# *1: use dijkstra to calculate the shortest paths

def take_input():
    n,m = map(int,input().split())
    lst = []
    dic = defaultdict(list)
    for _ in range(m):
        lst.append(list(map(int,input().split())))
    lst.sort(key = lambda x:x[3])
    for i in range(m):
        p1,p2,l,c = lst[i]
        dic[p1].append((p2,l,c))
        dic[p2].append((p1,l,c))
    return n,m,dic

n,m,dic = take_input()
print(n,m,dic)