def Chances_of_Winning(favourite_team,score,games):
    
    results = [score]
    for game in games:
        a,b = game
        chances = [(3,0),(0,3),(1,1)]
        arr = []
        for old_score in results:
            for chance in chances:
                new_socre = old_score[:]
                new_socre[a] += chance[0]
                new_socre[b] += chance[1]
                arr.append(new_socre)
        results = arr
    answer = 0
    for result in results:
        favourite_score = result[favourite_team]
        for i in range(1,len(result)):
            if i != favourite_team and result[i] >= favourite_score:
                answer -= 1
                break
        answer += 1
    return answer
            
                    


def take_input():
    favourite_team = int(input())
    played_games = int(input())
    score = [0] * 5
    games = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    for _ in range(played_games):
        a,b,sa,sb = map(int,input().split())
        games.remove((a,b))
        if sa>sb:
            score[a] += 3
        elif sa < sb:
            score[b] += 3
        else:
            score[a] += 1
            score[b] += 1
    return favourite_team,score,games

favourite_team,score,games = take_input()
print( Chances_of_Winning(favourite_team,score,games))