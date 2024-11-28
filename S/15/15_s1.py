def main(lst):
    return sum(lst)

def take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        a = int(input())
        if lst:
            if a == 0:
                lst.pop(-1)
            else:
                lst.append(a)
                
        else:
            lst.append(a)
    return lst

lst = take_input()
print(main(lst))