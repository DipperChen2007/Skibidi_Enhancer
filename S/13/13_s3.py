# 1. 计算已经完成的比赛分数
# [1, 10, 5, 21]
def Chances_of_Winning(favorite,score,games):
    rturn = 0
# 2. 模拟还没进行的比赛，生成不同结果的分数
# [score 1] [score 2] ...
    check_answer = [score]
    for game in games:           
        a,b = game
        arr = []
        for old_socre in check_answer:      
            for result in [(3, 0),(0, 3), (1, 1)]:
                new_scores = old_socre[:]
                new_scores[a] += result[0]
                new_scores[b] += result[1]
                arr.append(new_scores)
        check_answer = arr
    for answer in check_answer:
        for i in range(1,len(answer)):
            if i != favorite and answer[i] >= answer[favorite]:
                rturn -=1 
                break
        rturn += 1
    return rturn

# 3
# 3
# 1 3 7 5
# 3 4 0 8
# 2 4 2 2
# [3, 1, 0, 4]
#  [(1, 2), (1, 4), (2, 3)]
# (1, 2)
# [6, 1, 0, 4] [3, 4, 0, 4] [4, 2, 0, 4]
# (1, 4)

# 3. 从所有模拟结果中找出fav team胜利的次数

def take_input():
    score = [0]*5
    games = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    favorite = int(input())
    game = int(input())
    for _ in range(game):
        a,b,a_score,b_score = (list(map(int,input().split())))  
        games.remove((a,b))
        if a_score>b_score:
            score[a] += 3
        elif a_score<b_score:
            score[b] += 3
        else:
            score[a] += 1
            score[b] += 1
    return favorite,score,games


favorite,score,games = take_input()
print(Chances_of_Winning(favorite,score,games))