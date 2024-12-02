def area(n,h,w):
    answer = 0
    for i in range(n):
        h_1,h_2 = h[i],h[i + 1]
        b = w[i]
        answer += (h_1 + h_2) * b/2
    if int(answer) == answer:
        return int(answer)
    else:
        return answer

def take_input():
    n = int(input())
    h = list(map(int,input().split()))
    w = list(map(int,input().split()))
    return n,h,w

n,h,w = take_input()
print(area(n,h,w))