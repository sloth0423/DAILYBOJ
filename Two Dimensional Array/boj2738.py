import sys

input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
ls = list()
ls2 = list()
for i in range(x):
    a = input().split()
    ls.append([])
    for j in range(y):
        ls[i].append(int(a[j]))
for k in range(x):
    b = input().split()
    ls2.append([])
    for l in range(y):
        ls2[k].append(int(b[l]))
for m in range(x):
    for n in range(y):
        print(ls[m][n]+ls2[m][n], end = " ")
    print("")






