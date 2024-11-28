# CCC '20 S3 - Searching for Strings

needle = input()
haystack = input()
target = [0 for i in range(26)]
cur = [0 for i in range(26)]
base = 29
MOD = 59604644783353249
# ^ Found on wikipedia
good = 0
ans = set()

if len(needle) <= len(haystack):
    for i in needle:
        target[ord(i)-97] += 1
    hash = [0]
    for i in range(len(haystack)):
        hash.append(((hash[-1])*base+(ord(haystack[i])-97))%MOD)
    
    for i in range(len(needle)):
        cur[ord(haystack[i])-97]+=1
    
    for i in range(26):
        if target[i] == cur[i]:
            good += 1
    
    for i in range(len(haystack)-len(needle)+1):
        if good == 26:
            ans.add((hash[i+len(needle)]-(hash[i]*pow(base,len(needle),MOD))+MOD)%MOD)
        if i != len(haystack)-len(needle):
            if cur[ord(haystack[i])-97] == target[ord(haystack[i])-97]:
                good -= 1
            elif cur[ord(haystack[i])-97] == target[ord(haystack[i])-97]+1:
                good += 1
    
            cur[ord(haystack[i]) - 97] -= 1
    
            if cur[ord(haystack[i+len(needle)])-97] == target[ord(haystack[i+len(needle)])-97]:
                good -= 1
            elif cur[ord(haystack[i+len(needle)])-97] == target[ord(haystack[i+len(needle)])-97]-1:
                good += 1
            cur[ord(haystack[i + len(needle)]) - 97] += 1
    
    print(len(list(ans)))
else:
    print(0)