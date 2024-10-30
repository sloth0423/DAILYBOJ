import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
x = int(x)
for i in range(x):
    y = input()
    y1, y2 = y.split()
    y1 = int(y1)
    y2 = int(y2)
    print(y1+y2)

