import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n = int(input())
    while True:
        if n <= 2:
            print(2)
            break
        if n % 2 == 0:
            n += 1
            continue
        cnt = 0
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                cnt += 1
                n += 1
                break
        if cnt == 0:
            print(n)
            break

# 처음에 푼 코드
# 맞긴했지만 시간이 오래 걸려서 다시 풀어보기로 했다.
# 다시 생각해보니 2보다 큰 짝수는 무조건 소수가 아니므로
# 2보다 큰 짝수가 나오면 1을 더하고 continue를 사용하여 다시 while문을 돌게 하였다.
# 그렇게 되면 for 문을 돌 때 무조건 홀수가 들어오게 되므로 i가 2씩 커지게 하였다.
# 그 결과 실행시간이 반으로 줄었다.
# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     while True:
#         if n == 0 or n == 1:
#             print(2)
#             break
#         cnt = 0
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 cnt += 1
#                 n += 1
#                 break
#         if cnt == 0:
#             print(n)
#             break

# 시간을 줄이기 위해 찾아본 다른 사람이 푼 코드
# 최대한 시간을 줄여보려고 했으나
# 반복문과 조건문을 이용해서는 함수들을 이용하는 것의
# 실행시간을 따라잡을 수 없었다.
# 아래에 반복문의 isqrt(n)+3 부분에서 왜 +1이 아닌 +3을 했는가가 궁금했는데
# 곰곰이 생각해보았더니 isqrt(n)이 3보다 작을 때(4<=n<=8) 반복문이 돌아가지 않기 때문이다.
# 근데 다시 생각해보니
# 4,6,8은 짝수라서 그 전에 이미 걸려서 반복문이 안 돌아가고
# 5,7은 소수이기 때문에 반복문이 안 돌아가도 정답이기 때문에
# +1을 해도 상관은 없으나 의도를 잘 파악하기 위해 +3을 하는게 좋을 것 같다.
# import sys; input = sys.stdin.readline
# from math import ceil, isqrt
#
# def isprime(n):
#     if n < 2:
#         return False
#     if n < 4:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, isqrt(n)+1, 2):
#         if n%i == 0:
#             return False
#     return True
#
# def sol(n):
#     if n < 2:
#         return 2
#     if isprime(n):
#         return n
#     if n%2 == 0:
#         n += 1
#     while not isprime(n):
#         n += 2
#     return n
#
# for _ in range(int(input())):
#     print(sol(int(input())))


