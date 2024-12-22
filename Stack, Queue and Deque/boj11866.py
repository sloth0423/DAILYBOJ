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

# N, K = map(int, input().split())
# ls = list(range(1, N + 1))
# ls2 = list()
# idx = 0
# while ls:
#     idx += K - 1
#     if idx >= len(ls):
#         idx %= len(ls)
#     ls2.append(str(ls.pop(idx)))
# print(f'<{", ".join(ls2)}>')

