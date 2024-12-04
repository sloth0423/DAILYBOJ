import sys
input = lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())
s1 = set()
ans = list()
for _ in range(N):
    s1.add(input())
for _ in range(M):
    i = input()
    if i in s1:
        ans.append(i)
ans.sort()
print(len(ans))
print("\n".join(ans))

# 처음에 푼 코드
# 처음에는 보지 못한 사람도 set에 넣어서 비교를 했는데
# 굳이 set을 만들 필요가 없이 입력을 받자마자 비교해서
# ans에 넣으면 됐었다.
# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N, M = map(int,input().split())
# s1 = set()
# s2 = set()
# ans = list()
# for _ in range(N):
#     s1.add(input())
# for _ in range(M):
#     s2.add(input())
# for i in s1:
#     if i in s2:
#         ans.append(i)
# ans.sort()
# print(len(ans))
# print("\n".join(ans))