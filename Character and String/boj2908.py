import sys

input = lambda: sys.stdin.readline().rstrip()

x, y = input().split()

x = list(x)
y = list(y)

print(x,y)

x[0], x[2] = x[2], x[0]
y[0], y[2] = y[2], y[0]

x = int(''.join(x))
y = int(''.join(y))

if x > y :
    print(x)
else:
    print(y)
