from collections import deque

N = int(input())
dq = deque()
for i in range(1, N):
    dq.append(i)
n = N
while dq:
    dq.append(n)
    dq.popleft()
    n = dq.popleft()
print(n)
