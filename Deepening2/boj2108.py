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

# 최빈값을 찾는 법을 인터넷에 검색해서 복붙한 것인데
# 이해는 되는데 조금 더 생각해 보아야겠다.
# 일단 지금 생각한 것으로는 index함수가 맨 처음으로 만나는 index를 리턴하므로
# 배열의 리턴한 index를 0으로 만들고 다시 index함수를 사용하여 구한다던가...
# 반올림은 내가 만들었는데 그냥 round함수 사용하면 되더라..;;

