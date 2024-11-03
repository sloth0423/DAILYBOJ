import sys

input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
z = input()
z = z.split()
ls = []
for i in range(x):
    if int(z[i]) < y:
        ls.append(z[i])
for j in range(len(ls)):
    print(ls[j], end = " ")