def Computer_Purchase(lsts):
    lsts.sort(key = lambda x:x[1])
    lsts.sort(key = lambda x:x[0],reverse = True)
    if len(lsts) > 0:
        print(lsts[0][1])
    if len(lsts) > 1:
        print(lsts[1][1])
        


def Take_input():
    n = int(input())
    lsts = []
    for _ in range(n):
        name,r,s,d = input().split()
        lsts.append(((2 * int(r) + 3 * int(s) + int(d)),name))
    return lsts

lsts = Take_input()
Computer_Purchase(lsts)