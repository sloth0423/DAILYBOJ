import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ls = list()
for _ in range(N):
    x, y = map(int, input().split())
    ls.append([x, y])
ls.sort()
for i in range(N):
    print(f"{ls[i][0]} {ls[i][1]}")