import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ls = list(map(int, input().split()))
stack = []
cnt = 1

for i in ls:
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1

    if i == cnt:
        cnt += 1
    else:
        stack.append(i)

while stack and stack[-1] == cnt:
    stack.pop()
    cnt += 1

if not stack:
    print("Nice")
else:
    print("Sad")