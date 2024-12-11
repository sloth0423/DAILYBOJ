import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
ls = list(int(input()) for _ in range(T))
m = max(ls)
soe = [True] * (m+1) # sieve of Eratosthenes
srm = int(m**0.5)+1 # square root m
for i in range(3, srm, 2):
    if soe[i]:
        soe[i*i::2*i] = [False] * len(range(i*i, m, 2*i))
primes = [2] + [i for i in range(3, m, 2) if soe[i]]
sop = set(primes)
for j in ls:
    n = 0
    for k in primes:
        if k > j//2:
            break
        else:
            if j - k in sop:
                n += 1
    print(n)

# 처음에 푼 코드
# 처음에는 에라토스테네스의 체를 만드는 과정에서 중복되는 조건들이 너무 많았고
# set에서 찾지도 않아서 시간 초과가 계속 났다.
# 하지만 다른 사람이 푼 코드를 참조해서 중복되는 조건들을 빼고
# N - 테스트케이스가 소수인지 찾는 과정에서 소수들을 set에 넣고 판별하니
# 실행 시간이 많이 줄었다.

# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# def getPrimes(N):
#     ls = [True]*(N+1)
#     ls2 = []
#     ls[0],ls[1]  = False, False
#     for i in range(len(ls)):
#         if ls[i]:
#             ls[i*i::i] = [False] * (len(range(i*i, N+1, i)))
#             ls2.append(i)
#     return ls2
# def cntCases(n, ls, N):
#     for i in ls:
#         if i < (N//2 +1):
#             if N - i in ls:
#                 n += 1
#     return n
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     ls = getPrimes(N)
#     n = 0
#     cnt = cntCases(n, ls, N)
#     print(cnt)