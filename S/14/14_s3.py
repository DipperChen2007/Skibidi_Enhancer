def main(td_lst):
    for lst in td_lst:
        if check(lst):
            print("Y")
        else:
            print("N")
        

def check(lst):
    lst.reverse()
    branch = []
    count = 1
    for e in lst:
        branch.append(e)
        while branch and branch[-1] == count:
            branch.pop()
            count += 1
    print(branch)       
    if branch:
        return False
    else:
        return True


def take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append([])
        for __ in range(int(input())):
            lst[-1].append(int(input()))
    return lst
        
lst = take_input()
main(lst)