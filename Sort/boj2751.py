import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())
ls = list()
for _ in range(x):
    ls.append(int(input()))
ls.sort()
for i in range(x):
    print(ls[i])
