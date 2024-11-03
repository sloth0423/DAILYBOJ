import sys

input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
ls = list()
for i in range(x):
    ls.append(0)
for j in range(y):
    first, last, number = map(int,input().split())
    for k in range(x):
        if k >= (first-1) and k <= (last-1):
            ls[k] = number
for l in range(x):
    print(ls[l], end = " ")