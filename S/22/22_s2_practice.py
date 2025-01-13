def Good_groups(must_in,must_not_in,groups):
    answer = len(must_in)
    for group in groups:
        for student_1,student_2 in must_in:
            if student_1 in group and student_2 in group:
                answer -= 1
        for student_1,student_2 in must_not_in:
            if student_1 in group and student_2 in group:
                answer += 1
                
    return answer


def take_input():
    x = int(input())
    must_in = []
    for i in range(x):
        must_in.append(list(input().split()))
    y = int(input())
    must_not_in = []
    for i in range(y):
        must_not_in.append(list(input().split()))
    g = int(input())
    groups = []
    for i in range(g):
        groups.append(list(input().split()))
    return must_in,must_not_in,groups

must_in,must_not_in,groups = take_input()
print(Good_groups(must_in,must_not_in,groups))