from collections import Counter
def SFS(string,long_string):
    s_c = Counter(string)
    answer = set()
    for i in range(len(long_string) - len(string)+1):
        s = ""
        for j in range(i,i + len(string)):
            s += long_string[j]
        if Counter(s) == s_c:
            answer.add(s)
            
    return len(answer)
            
def take_input():
    string = input()
    long_string = input()
    return string,long_string
string,long_string = take_input()
print(SFS(string,long_string ))
