def GG(be_in_same,not_be_in_same,groups):
    answer=0
    if be_in_same:
        for c in be_in_same:
            answer += 1
            for group in groups:
                if set(c).issubset(group):
                    answer -= 1
    if not_be_in_same:
        for cc in not_be_in_same:
            for group in groups:
                if set(cc).issubset(group):
                    answer += 1
    return answer
        

def take_input():
    x = int(input())
    be_in_same = []
    for _ in range(x):
        be_in_same.append(list(input().split()))
    y = int(input())
    not_be_in_same = []
    for j in range(y):
        not_be_in_same.append(list(input().split()))
    g = int(input())
    groups = []
    for jj in range(g):
        groups.append(list(input().split()))
        
    return be_in_same,not_be_in_same,groups

be_in_same,not_be_in_same,groups = take_input()
print(GG(be_in_same,not_be_in_same,groups))
