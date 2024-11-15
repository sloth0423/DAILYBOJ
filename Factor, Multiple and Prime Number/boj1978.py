import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())

ls = list(map(int, input().split()))
ls2 = list()
for i in range(x):
    if ls[i] != 1 and ls[i] != 2:
        cnt = 0
        for j in range(1, int(ls[i]**0.5)+2):
            if ls[i] % j == 0:
               cnt += 1
        if cnt == 1:
            ls2.append(ls[i])
    if ls[i] == 2:
        ls2.append(ls[i])
print(len(ls2))
