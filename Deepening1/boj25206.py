import sys

input = lambda: sys.stdin.readline().rstrip()

sum = 0.0
sum2 = 0.0
for _ in range(20):
    x, y, z = input().split()
    y = float(y)
    if z == 'A+':
        sum += y
        sum2 += 4.5*y
    elif z == 'A0':
        sum += y
        sum2 += 4.0*y
    elif z == 'B+':
        sum += y
        sum2 += 3.5*y
    elif z == 'B0':
        sum += y
        sum2 += 3.0*y
    elif z == 'C+':
        sum += y
        sum2 += 2.5*y
    elif z == 'C0':
        sum += y
        sum2 += 2.0*y
    elif z == 'D+':
        sum += y
        sum2 += 1.5*y
    elif z == 'D0':
        sum += y
        sum2 += 1.0*y
    elif z == 'F':
        sum += y
        sum2 += 0.0
if sum != 0:
    print(sum2/sum)

# 다른 사람이 쓴 코드
# 학점을 리스트에 넣고 학점의 index에 0.5를 곱해서 과목평점을 얻는 방법
# D0와 F사이에 0.5가 없으니 빈 문자열 '' 하나를 넣는게 대단했다.

# import sys
# sum = 0
# class_sum = 0
# for _ in range(20):
#     box = ['F', '', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
#
#     subject, score, grade = input().split()
#     if grade != "P":
#         sum += float(score) * box.index(grade) * 0.5
#         class_sum += float(score)
#
# print(sum / class_sum)
