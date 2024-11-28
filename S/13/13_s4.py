def takeinput():
    dic = {}
    students, pairs = [int(i) for i in input().split()]
    for _ in range(pairs):
        high, low = [int(i) for i in input().split()]
        if high in dic:
            dic[high].append(low)
        else:
            dic[high] = [low]
            
    higher, lower = [int(i) for i in input().split()]
    return higher, lower, dic

def whoIsTaller(higher, lower, dic):
    visited = set()
    visited.add(higher)
    frontier = [higher]
    while frontier:
        current = frontier.pop()
        if current == lower:
            return True
        
        for student in dic[current]:
            if student not in visited:
                visited.add(student)
                frontier.append(student)
    return False

higher, lower, dic = takeinput()

if whoIsTaller(higher, lower, dic):
    print("yes")
elif whoIsTaller(lower, higher, dic):
    print("no")
else:
    print("unknown")
    