import sys

input = lambda: sys.stdin.readline().rstrip()

while(1):
    try:
        x, y = map(int, input().split())
        print(x+y)
    except:
        break