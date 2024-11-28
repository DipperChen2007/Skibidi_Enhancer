def Aromatic_Numbers(lst):
    # I	V	X	L	C	D	M
    #1	5	10	50	100	500	1000
    
    #3M1D2C
    #[('3', 'M'), ('1', 'D'), ('2', 'C')]
    answer = 0
    symbol_base = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(len(lst) -1):
        current_A,current_R = lst[i]
        next_A,next_R = lst[i + 1]
        if symbol_base[next_R] <= symbol_base[current_R]:
            answer += current_A*(symbol_base[current_R])
        else:
            answer -= current_A*(symbol_base[current_R])
    last_A,last_R = lst[-1]
    answer += last_A*(symbol_base[last_R])
    return answer

def take_input():
    s = input()
    lst = []
    for i in range(len(s)):
        if i%2 != 0:
            lst.append((int(s[i - 1]),s[i]))
    return lst
lst = take_input()
print(Aromatic_Numbers(lst))