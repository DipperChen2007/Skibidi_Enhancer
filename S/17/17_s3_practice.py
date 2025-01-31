from collections import defaultdict

def find_max_board(lst_of_boards):
    dp = defaultdict(list)
    for i in range(len(lst_of_boards)):
        for j in range(i + 1,len(lst_of_boards)):
            dp[i + 1].append(lst_of_boards[i] + lst_of_boards[j])
    print(dp)
    
    
    

def take_input():
    n = int(input())
    lst_of_boards = list(map(int,input().split()))
    return n,lst_of_boards

n,lst_of_boards = take_input()
find_max_board(lst_of_boards)