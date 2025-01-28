from collections import Counter

def main(points,m):
    answer = 0
    r = m/2
    
    for i in range(len(points)-2):
        k_1,v_1 = points[i]
        for j in range(i+1,len(points) - 1):
            k_2,v_2 = points[j]
            if abs(k_2 - k_1) < r:      
                for k in range(j+1,len(points)):
                    k_3,v_3 = points[k]
                    if abs(k_3 - k_1) > r and abs(k_3 - k_2) < r:
                        answer += v_1*v_2*v_3               
    return answer

def take_input():
    n,m = map(int,input().split())
    points = list(map(int,input().split()))
    points = Counter(points)
    points = sorted(points.items())
    return points,m   



points,m = take_input()
print(main(points,m))