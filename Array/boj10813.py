import sys

input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
ls = list()
for i in range(x):
    ls.append(i+1)
for j in range(y):
    basketNum1, basketNum2 = map(int, input().split())
    ls[basketNum1-1], ls[basketNum2-1] = ls[basketNum2-1], ls[basketNum1-1]
for k in range(x):
    print(ls[k], end = " ")