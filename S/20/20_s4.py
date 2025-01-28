from collections import Counter

def Swapping_Seats(s):
    rounded_s = s*2
    prefix_a = [0]*len(rounded_s)
    prefix_b = [0]*len(rounded_s)
    prefix_c = [0]*len(rounded_s)
    for i in range(len(rounded_s)):
        prefix_a[i] = prefix_a[i-1] + (rounded_s[i] == "A")
        prefix_b[i] = prefix_b[i-1] + (rounded_s[i] == "B")
        prefix_c[i] = prefix_c[i-1] + (rounded_s[i] == "C")
    counter = Counter(s)
    num_a = counter["A"]
    num_b = counter["B"]
    num_c = counter["C"] 
    non_rational_positions = float("inf")
    for i in range(len(s)):
        good_a = prefix_a[i+num_a] - prefix_a[i]
        good_b = prefix_b[i+num_b] - prefix_b[i]
        good_c = prefix_c[i+num_c] - prefix_c[i]
        bad_a = num_a - good_a
        bad_b = num_b - good_b
        bad_c = num_c - good_c
        non_rational_positions = min(non_rational_positions,bad_a,bad_b)
    return non_rational_positions


def compare_strings(s1,s2,offset):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i+offset]:
            diff += 1
    return diff//2 + diff%2
    
def take_input():
    s = input()
    return s

s = take_input()
print(Swapping_Seats(s))