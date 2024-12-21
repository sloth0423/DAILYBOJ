from collections import deque

N, K = map(int, input().split())
dq = deque(range(1, N+1))
ls = list()
while True:
    if len(dq) != 0:
        for _ in range(K):
            n = dq.popleft()
            dq.append(n)
        p = dq.pop()
        ls.append(str(p))
    else:
        break
print(f"<{", ".join(ls)}>")


