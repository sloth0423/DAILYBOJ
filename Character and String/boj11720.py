import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
x = int(x)
y = input()
rslt = 0
for i in range(x):
    rslt += int(y[i])
print(rslt)
