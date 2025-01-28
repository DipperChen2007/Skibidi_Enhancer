def main(points,m):
    answer = 0
    r = m/2
    for i in range(len(points) - 2):
        matching_points = [points[i]]
        for j in range(i+1,len(points) - 1):
            if points[j] - matching_points[0] <= r:
                matching_points.append(points[j])
            for k in range(j+1,len(points)):
                if points[k] - matching_points[0] >= r and points[k] - matching_points[1] <= r:
                    matching_points.append(points[k])
        if len(matching_points) == 3:
            answer += 1
    return answer

def take_input():
    n,m = map(int,input().split())
    points = list(map(int,input().split()))
    return points,m    

points,m = take_input()
print(main(points,m))
        
