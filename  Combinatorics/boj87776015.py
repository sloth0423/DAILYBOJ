N, K = map(int,input().split())
rslt = 1
for i in range(K+1, N+1):
    rslt *= i
for j in range(1, N - K + 1):
    rslt //= j
print(rslt)