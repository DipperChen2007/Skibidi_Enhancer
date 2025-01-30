from collections import defaultdict

def GG(must_be_in_same,must_not_be_in_same,groups):
    answer = 0
    for group in groups:
        groupSet = set(group)
        for i in range(len(group)):
            sA = group[i]
            for s in must_be_in_same[sA]:
                if s not in groupSet:
                    answer += 1
            for j in range(len(group)):
                sB = group[j]
                if sB in must_not_be_in_same[sA]:
                    answer += 1
    return answer//2

def take_input():
    n = int(input())
    must_be_in_same = defaultdict(set)
    for _ in range(n):
        studentA,studentB = input().split()
        must_be_in_same[studentA].add(studentB)
        must_be_in_same[studentB].add(studentA)
    m = int(input())
    must_not_be_in_same = defaultdict(set)
    for _ in range(m):
        studentA,studentB = input().split()
        must_not_be_in_same[studentA].add(studentB)
        must_not_be_in_same[studentB].add(studentA)
    g = int(input())
    groups = []
    for _ in range(g):
        groups.append(list(input().split()))
    return must_be_in_same,must_not_be_in_same,groups

must_be_in_same,must_not_be_in_same,groups = take_input()
print(GG(must_be_in_same,must_not_be_in_same,groups))