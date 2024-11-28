def Huffman_Encoding(dic,s):
    answer = ""
    i = 0
    while i < len(s):
        for j in range(i,len(s)):
            check = s[i:j + 1]
            if check in dic:
                answer += dic[check]                
                i = j + 1
                break

    return answer

def take_input():
    n = int(input())
    dic = {}
    for _ in range(n):
        letter,number = input().split()
        dic[number] = letter
    s = input()
    return dic,s

dic,s = take_input()
print(Huffman_Encoding(dic,s))

