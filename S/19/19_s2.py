def PAP(lst):
    answer = []
    for e in lst:
        a = b = e
        if number_is_prime(e):
            answer.append([a,b])
        else:
            while not number_is_prime(a) or not number_is_prime(b):
                a-=1
                a+=1
            answer.append([a,b])
    
    for l in answer:
        print(*l)
        

def number_is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def take_input():
    t = int(input())
    lst = []
    for _ in range(t):
        lst.append(int(input()))
    return lst 

lst = take_input()
PAP(lst)