from collections import Counter

def Ragaman(f,s):
    f_c = Counter(f)
    s_c = Counter(s)
    for e in f_c:
        if s_c[e] > f_c[e]:
            return "N"
        elif s_c[e] < f_c[e]:
            if "*" in s_c:
                if f_c[e] - s_c[e] > s_c["*"]:
                    return "N"
                else:
                    s_c["*"] -= f_c[e] - s_c[e]
            else:
                return "N"
    
    return "A"
                    
            
            
def take_input():
    f = input()
    s = input()
    return f,s

f,s = take_input()
print(Ragaman(f,s))