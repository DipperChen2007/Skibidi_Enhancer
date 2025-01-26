def main(m,matrix):
    answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] >= m:
                answer += 1  
    return answer

def take_input():
    n = int(input())
    m = int(input())
    points = []
    smallest_x = float('inf')
    smallest_y = float('inf')
    biggest_x = 0
    biggest_y = 0
    for _ in range(n):
        a,b,c,d,t = map(int,input().split())
        smallest_x = min(smallest_x,a)
        smallest_y = min(smallest_y,b)
        biggest_x = max(biggest_x,c)
        biggest_y = max(biggest_y,d)        
        points.append((a,b,c,d,t))
    row = biggest_x - smallest_x + 1
    col = biggest_y - smallest_y + 1
    matrix = [[0 for _ in range(col)] for _ in range(row)]
    for a,b,c,d,t in points:
        for i in range(a - smallest_x,c - smallest_x):
            for j in range(b - smallest_y,d - smallest_y):
                matrix[j][i] += t
    return m,matrix

m,matrix = take_input()
print(main(m,matrix))
