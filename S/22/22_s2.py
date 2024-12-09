def GG(be_in_same,not_be_in_same,groups):
    answer = 0
    for group in groups:
        # size(3)
        groupSet = set(group)
        for i in range(len(group)):
            # size(3)
            sA = group[i]
            for s in be_in_same[sA]:
                if s not in groupSet:
                    answer +=1
            for j in range(len(group)):
                sB = group[j]
                if sB in not_be_in_same[sA]:
                    answer += 1



        # if be_in_same:
        # size(X) 
        #     for c in be_in_same:
        #         if set(c).issubset(group):
        #             answer -= 1
        # size(Y) 
        # if not_be_in_same:
        #     for cc in not_be_in_same:
        #         if set(cc).issubset(group):
        #             answer += 1
                    
    return answer // 2
        
from collections import defaultdict
def take_input():
    x = int(input())
    be_in_same = defaultdict(set)
    for _ in range(x):
        studentA, studentB = input().split()
        be_in_same[studentA].add(studentB)
        be_in_same[studentB].add(studentA)
    y = int(input())
    not_be_in_same = defaultdict(set)
    for j in range(y):
        studentA, studentB = input().split()
        not_be_in_same[studentA].add(studentB)
        not_be_in_same[studentB].add(studentA)
    g = int(input())
    groups = []
    for jj in range(g):
        groups.append(list(input().split()))
        
    return be_in_same,not_be_in_same,groups

be_in_same,not_be_in_same,groups = take_input()
print(GG(be_in_same,not_be_in_same,groups))

# [[a, c], [a, b]]
# {
#   a: {c, b},
#   c: {a},
#   b: {a}
# }

