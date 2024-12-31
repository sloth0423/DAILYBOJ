def fac(N):
    if N == 0 or N == 1:
        return 1
    else:
        N = N * fac(N-1)
        return N
N = int(input())
print(fac(N))