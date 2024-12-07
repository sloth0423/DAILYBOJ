import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
ls = list(int(input()) for _ in range(N))
gcd = ls[1] - ls[0]
for i in range(2,N):
    A, B = gcd, ls[i] - ls[i-1]
    while A % B != 0:
        R = A % B
        A = B
        B = R
    gcd = B
print(((ls[N-1]-ls[0])//gcd)-N+1)

# 두번째로 푼 코드
# 나무들 사이의 거리를 list에 넣지는 않았지만
# 최대공약수를 간격으로 하는 나무들을 set에 넣어서 메모리 초과가 났다.
# 그냥 나무들의 수만 출력하면 되기 때문에
# 나무들을 전부 리스트에 넣을 필요가 없었다.

# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N = int(input())
# ls = list(int(input()) for _ in range(N))
# lcd = ls[1] - ls[0]
# for j in range(2,N):
#     A, B = lcd, ls[j] - ls[j-1]
#     while A % B != 0:
#         R = A % B
#         A = B
#         B = R
#     lcd = B
# ls2 = set(k for k in range(ls[0], ls[N-1],lcd))
# ls2 = ls2 - set(ls)
# print(len(ls2))

# 첫 번째로 푼 코드
# list에 모든 요소를 넣고
# 나무들 사이의 거리도 list에 넣고
# 최대공약수를 구해서 첫번째 나무부터 마지막 나무까지
# 최대공약수를 간격으로 하는 나무들도 set에 넣어서
# 메모리 초과가 났다.
# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N = int(input())
# ls = list(int(input()) for _ in range(N))
# ls2 = list(set(ls[i]- ls[i-1] for i in range(1, N)))
# lcd = ls2[0]
# for j in range(1,len(ls2)):
#     A, B = lcd, ls2[j]
#     while A % B != 0:
#         R = A % B
#         A = B
#         B = R
#     lcd = B
# ls3 = set(k for k in range(ls[0], ls[N-1],lcd))
# ls3 = ls3 - set(ls)
# print(len(ls3))
