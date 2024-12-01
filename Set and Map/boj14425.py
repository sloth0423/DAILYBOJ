import sys
input = lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())
sumNum = 0
set1 = set(input() for _ in range(N))

for _ in range(M):
    if input() in set1:
        sumNum += 1
print(sumNum)

# 다 풀고 생각해보니 굳이 리스트를 만들 필요가 없었다.
# 그냥 차례로 나오는 값을 비교하면 될 것 같다.

# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N, M = map(int, input().split())
# sumNum = 0
# set1 = set(input() for _ in range(N))
# ls = list(input() for _ in range(M))
#
# for i in ls:
#     if i in set1:
#         sumNum += 1
# print(sumNum)