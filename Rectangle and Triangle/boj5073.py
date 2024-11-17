import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    x, y, z = map(int, input().split())
    ls = [x, y, z]
    if x + y + z == 0:
        break
    elif max(ls) >= sum(ls) - max(ls):
        print("Invalid")
    elif len(set(ls)) == 1:
        print("Equilateral")
    elif len(set(ls)) == 2:
        print("Isosceles")
    else:
        print("Scalene")

# 이 문제 이렇게 하면 틀렸다고 해야하는데 맞다고 함
# 3 1 2 넣으면 Invalid 나와야 하는데 Scalene 나옴 근데 맞다고 함
# 위 코드는 고친 코드 아래 코드는 오류인데 정답 코드
# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# while True:
#     x, y, z = map(int, input().split())
#     ls = [x, y, z]
#     if x + y + z == 0:
#         break
#     elif max(ls) >= ls[0] + ls[1]:
#         print("Invalid")
#     elif len(set(ls)) == 1:
#         print("Equilateral")
#     elif len(set(ls)) == 2:
#         print("Isosceles")
#     else:
#         print("Scalene")