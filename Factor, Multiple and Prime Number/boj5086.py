import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x % y == 0:
        print("multiple")
    elif y % x == 0:
        print("factor")
    else:
        print("neither")

