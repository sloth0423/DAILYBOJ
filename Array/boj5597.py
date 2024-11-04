import sys

input = lambda: sys.stdin.readline().rstrip()

ls = list()
ls2 = list()
for i in range(28):
    x = input()
    x = int(x)
    ls.append(x)
for j in range(1, 31):
    try:
        ls.index(j)
    except ValueError as e:
        print(j)