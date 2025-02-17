def Marble(k,marble):
    answer = 0
    for i in range(len(marble) - 1):
        if marble[i] == 1 and marble[i + 1] == 1:
           
            check = i + 1
            while check < len(marble) and marble[check] == 1:
                check += 1
            for j in range(i,check - 1):
                marble[j] = 0
            answer += 1
    for i in range(len(marble)):
        if marble
             
    return answer
        

def take_input():
    n,k = map(int,input().split())
    m = input()
    marble = []
    for s in m:
        marble.append(int(s))
    return k,marble

k,marble = take_input()
print(Marble(k,marble))