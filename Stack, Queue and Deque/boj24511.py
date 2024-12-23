import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
sOrQ = list(map(int,input().split()))
eOfSOrQ = list(map(int, input().split()))
M = int(input())
iE = list(map(int,input().split()))
rslt = list(eOfSOrQ[i] for i in range(N) if sOrQ[i] == 0)
rslt.reverse()
rslt = rslt + iE
rslt = rslt[:M]
print(" ".join(map(str, rslt)))

# 시간초과가 계속 나서 곰곰이 생각해 봤더니
# queuestack에 있는 모든 요소를 확인할 필요가 없이
# 그냥 queue에 있는 요소들만 나오고
# 만약 queue에 있는 요소들이 다 나왔다면 처음에
# 삽입했던 순서대로 요소들이 나온다.
# 처음에 푼 방법
# import sys
#
# input = lambda: sys.stdin.readline().rstrip()
#
# N = int(input())
# sOrQ = list(map(int,input().split()))
# eOfSOrQ = list(map(int, input().split()))
# M = int(input())
# iE = list(map(int,input().split()))
# rslt = list()
# for i in range(M):
#     e = iE[i]
#     for j in range(N):
#         if sOrQ[j] == 0:
#             eOfSOrQ[j], e = e, eOfSOrQ[j]
#     rslt.append(str(e))
# print(" ".join(rslt))