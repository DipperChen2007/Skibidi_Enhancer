def is_in_order(lst):

    for i in range(len(lst) - 1):

        if lst[i] == "" or lst[i + 1] == "":
            return False
        elif len(lst[i]) > 1:
            return False
        elif int(lst[i]) > int(lst[i + 1]):
            return False
        
        
    return True

def A_Coin_Game(lst):
    #create visited
    visited = set()
    #[3,2,1]
    #[23, ,1],[3,12, ]
    queue = [(lst,0)]
    
    #bfs
    while queue:
        state,count = queue.pop(0)
        # check if state was in visited
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        #check if state is in order
        if is_in_order(state):
            return count
        #process state
        for i in range(len(state)):
            #if current place != ""
            if state[i] != "":
            #1.left
            #[3,12, ]
            #[13,2, ]
            #if in range and smaller than left top
                if i != 0 and (state[i-1] == "" or int(state[i][0]) < int(state[i - 1][0])):
                    state_copy = state.copy()
                    state_copy[i - 1] = state_copy[i][0] + state_copy[i - 1]
                    state_copy[i] = state_copy[i][1:]
                    queue.append((state_copy,count + 1))
                #2.right
                #if in range and smaller than right top
                if i != len(state) - 1 and (state[i+1] == "" or int(state[i][0]) < int(state[i+1][0])):
                    state_copy = state.copy()
                    state_copy[i + 1] = state_copy[i][0] + state_copy[i + 1]
                    state_copy[i] = state_copy[i][1:]
                    queue.append((state_copy,count + 1))
    return "IMPOSSIBLE"   
 
#[["3","2","1"],["2","1"]]
def Take_input():
    lsts = []
    #check if current line is 0
    while int(input()) != 0:
        #add next line into the lst
        lsts.append(input().split())
    return lsts

lsts = Take_input()
for lst in lsts:
    print(A_Coin_Game(lst))



        
    
    
            
        
        
    