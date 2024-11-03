import sys

input = lambda: sys.stdin.readline().rstrip()

while (1):
    X = input()
    x, y = X.split()
    x = int(x)
    y = int(y)
    if (x == 0 and y ==0):
        break
    else:
        print(x+y)
