def fttt(s):
    n = int(s) + 1
    while not checking(str(n)):
        n += 1
    return n

def checking(year):
    lst = []
    for i in range(len(year)):

        if int(year[i]) in lst:
            return False
        else:
            lst.append(int(year[i]))
      
    return True
            
def take_input():
    s = input()
    return s

s = take_input()
print(fttt(s))