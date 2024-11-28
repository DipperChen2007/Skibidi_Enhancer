def English_or_French(s):
    tT = 0
    sS = 0
    for chr in s:
        if chr == "t" or chr == "T":
            tT += 1
        elif chr == "s" or chr == "S":
            sS += 1
    if sS >= tT:
        return "French"
    else: 
        return "English"

def take_input():
    s = ""
    n = int(input())
    for _ in range(n):
        s+=input()
    return s

s = take_input()
print(English_or_French(s))