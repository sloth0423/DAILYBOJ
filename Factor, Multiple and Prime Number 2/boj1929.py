def printPrime(s, e):
    n = s
    while n != (e+1):
        if n == 1:
            n += 1
            continue
        if n == 2:
            print(n)
            n += 1
            continue
        if n == 3:
            print(n)
            n += 1
            continue
        if n % 2 == 0 or n % 3 == 0:
            n += 1
            continue
        cnt = 0
        for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                cnt += 1
                n += 1
                break
        if cnt == 0:
            print(n)
            n += 1

import sys
input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
printPrime(M, N)

# 이 사람은 메모리는 조금 더 썼지만 실행시간이 많이 차이나서 가져왔는데
# 일단 마지막 숫자까지 모두 True인 배열을 만든 후
# 2부터 루트 N까지의 소수들의 배수를 False로 만들어서
# 소수들을 찾았다.
# 반복문을 도는 도중에 계속 비교 횟수를 줄여가서 시간이 많이 단축된 것같다.
#
# import sys
# from math import sqrt  # sqrt 함수 임포트
# input = lambda:sys.stdin.readline().rstrip()
#
# def find_primes(start, end):
#     # 모든 숫자를 일단 소수라고 표시
#     is_prime = [True] * (end + 1)
#     is_prime[0] = is_prime[1] = False
#
#     # 2부터 end의 제곱근까지만 확인하면 됨
#     # 예: end가 100이면 10까지만 확인하면 됨
#     sqrt_end = int(sqrt(end))
#
#     # 2부터 숫자를 키워가며 확인
#     for i in range(2, sqrt_end + 1):
#         if is_prime[i]:
#             # i가 소수라면, i의 배수들은 모두 소수가 아님
#             for j in range(i * 2, end + 1, i):
#                 is_prime[j] = False
#
#     # start부터 end까지 중에서 소수만 출력
#     for i in range(start, end + 1):
#         if is_prime[i]:
#             print(i)
# # 입력 받기
# start, end = map(int, input().split())
# find_primes(start, end)