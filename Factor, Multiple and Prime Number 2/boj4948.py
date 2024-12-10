def countPrime(n):
    e = 2*n
    s = 0
    n += 1
    while n != (e+1):
        if n == 1:
            n += 1
            continue
        if n == 2:
            s += 1
            n += 1
            continue
        if n == 3:
            s += 1
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
            s += 1
            n += 1
    print(s)
import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 0:
        break
    else:
        countPrime(n)
        continue

# 오늘은 에라토스테네스의 체라는 알고리즘에 대해 공부하였다.
# 이 알고리즘은 매우 쉬운 것 처럼 보이나 나는 이해하는데 꽤나 오랜 시간이 걸렸다.
# 특정한 수 k가 주어질 때, n이 2부터 시작해서 n이 k의 제곱근이 될 때까지 n을 1씩
# 증가시키며 계속 k보다 작은 n을 제외한 n의 배수를 지우는 방법이다.
# 이게 되는 이유: 1을 제외한 모든 소수가 아닌 자연수들은
# 그보다 작은 소수로 적어도 한번은 나누어지기 때문이다.
# n이 k의 제곱근까지만 증가해도 되는 이유는
# n이 k의 제곱근+1이라고 하자.
# 그럼 n의 배수들 중 n*n보다 작은 수들은 이미 지워진 상태이다.
# (2부터 n까지 배수들을 지웠기 때문이다.)
# 그리고 n*n은 k보다 크므로 지울 필요가 없다.
# 그러므로 n은 k의 제곱근까지만 증가해도 된다.
# 이 코드를 친 후에 알게 된 알고리즘이라 다음 문제부터 이 알고리즘을 사용하겠다.
# 이 알고리즘이 특정한 수 까지의 소수를 찾는 알고리즘 중에서는 가장 빠르다고 한다.
