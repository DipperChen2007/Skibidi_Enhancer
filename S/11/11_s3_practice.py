def take_input():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int,input().split())))