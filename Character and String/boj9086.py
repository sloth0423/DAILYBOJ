import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())

for _ in range(x):
    y = input()
    print(y[0],y[-1],sep = '')
    # print(y[0], end = "")
    # print(y[-1])

