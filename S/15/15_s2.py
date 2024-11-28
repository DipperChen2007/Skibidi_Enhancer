def Jerseys(jerseys,atheltes):
    answer = 0
    s = {
        "S":5,
        "M":10,
        "L":15
    }
    for preferred_size,number in atheltes:
        preferred_number = int(number)
        jersey_size,used = jerseys[preferred_number-1]
        if used == 0:
            if s[jersey_size]>=s[preferred_size]:
                answer += 1
                jerseys[preferred_number-1] = (jersey_size,used+1)
    return answer
        
    

def take_input():
    j = int(input())
    a = int(input())
    jerseys = []
    atheltes = []
    for _ in range(j):
        jerseys.append((input(),0))
    for i in range(a):
        atheltes.append(list(input().split()))
    return jerseys,atheltes

jerseys,atheltes = take_input()
print(Jerseys(jerseys,atheltes))
        