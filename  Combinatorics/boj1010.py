import sys
input = lambda:sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    rslt = 1
    for i in range(N+1, M+1):
        rslt *= i
    for j in range(1, M - N + 1):
        rslt //= j
    print(rslt)