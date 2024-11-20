import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0
result = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cnt = ls[i] + ls[j] + ls[k]
            if M - cnt >= 0:
                if cnt > result:
                    result = cnt
print(result)
# 이 문제를 푼 뒤 똑같은 코드를 여러 번 넣어봤는데
# 넣을 때마다 실행시간이 달랐다.
# 왜 그런걸까..