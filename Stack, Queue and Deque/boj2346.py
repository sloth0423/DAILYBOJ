import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ls = list(map(int, input().split()))
ls2 = list(i for i in range(N))
ls3 = list()
idx = 0
for _ in range(N):
    ls3.append(str(ls2.pop(idx)+1))
    n = ls.pop(idx)
    length = len(ls2)
    if length != 0:
        if n > 0:
            idx = (idx + n - 1) % length
        else:
            idx = (idx + n) % length
    else:
        break
print(" ".join(ls3))