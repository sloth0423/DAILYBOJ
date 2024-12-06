import sys
import math
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A,B))

# 처음에 푼 코드
# 찾아보니 math 라이브러리에 최소공배수를 찾아주는 함수가 있었다.
# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     m = min(A, B) + 1
#     for i in range(m, 1, -1):
#         if i == 1:
#             print(A*B)
#         elif A % i == 0 and B % i == 0:
#             print(i*(A/i)*(B/i))