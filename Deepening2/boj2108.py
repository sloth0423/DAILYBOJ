import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ls = sorted(list(int(input()) for _ in range(N)))
S = sum(ls)
if S >= 0:
    a = str(int(S/N*10))
    if int(a[-1]) >= 5:
        a = (int(a)//10)+1
    else:
        a = int(a)//10
else:
    S = abs(S)
    a = str(int(S / N * 10))
    if int(a[-1]) >= 5:
        a = (int(a) // 10) + 1
    else:
        a = int(a) // 10
    a = a * -1
m = ls[(N//2)]
f = Counter(ls)

b = f.most_common()

if len(ls) >1:
    if b[0][1] == b[1][1]:
        mode = b[1][0]
    else:
        mode = b[0][0]
else:
    mode = ls[0]
r = ls[-1] - ls[0]
print(a)
print(m)
print(mode)
print(r)

