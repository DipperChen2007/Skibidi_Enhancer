def Multiple_Choice(s,c):
    answer = 0
    for i in range(len(s)):
        if s[i] == c[i]:
            answer += 1
    return answer


def take_input():
    s = []
    c = []
    n = int(input())

    for _ in range(n):
        s.append((input()))
    for _ in range(n):
        c.append((input()))
    return s,c

s,c = take_input()
print(Multiple_Choice(s,c))