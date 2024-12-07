# 유클리드 호제법에 대해 살짝 설명해 보겠다.
# A와 B가 있고 A > B 이고, A를 B로 나눈 나머지가 C라고 할 때
# 일단 B는 A를 나누어 떨어지게 할 수 없으므로 공약수가 아니다.
# B와 C사이의 모든 수는 결국 C를 못 나누므로 A를 나누어 떨어지게 할 수 없다.
# B를 C로 다시 나눴을 때 경우의 수는
# 나누어 떨어지거나 아니거나 두 가지 이다.
# 만약 나누어 떨어진다면 C는 B를 나누어 떨어지게 한 것이고
# A를 B로 나눈 나머지인 C는 당연히 나누어 떨어지게 할 것이므로
# C가 A와 B의 최대공약수가 된다.
# 만약 나누어 떨어지지 않는다면
# C는 B를 나누어 떨어지게 하지 못했으므로 A와 B의 공약수가 아니다.
# 그러므로 B를 C로 나눈 나머지로 C를 다시 나누어 본다.
# (나누어 떨어질 때까지 반복(나누다 보면 언젠가는 나누어 떨어지게 된다. 아무리
# 공약수가 없어도 결국에는 1을 서로의 공약수로 가지고 있기 때문이다.))
import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    AA, BB = map(int, input().split())
    A = AA
    B = BB
    while A % B != 0:
        R = A % B
        A = B
        B = R
    print(AA*BB//B)

# 두번째로 푼 코드
# 그냥 라이브러리를 사용하여 푸는 것은
# 공부가 안될 것 같아서 찾아보니 유클리드 호제법이라는
# 최대공약수를 찾아주는 알고리즘이 있었다.
# import sys
# import math
# input = lambda: sys.stdin.readline().rstrip()
#
# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     print(math.lcm(A,B))

# 처음에 푼 코드
# 시간 초과가 나서 찾아보니 math 라이브러리에 최소공배수를 찾아주는 함수가 있었다.
# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     m = min(A, B) + 1
#     for i in range(m, 1, -1):
#         if i == 1:
#             print(A*B)
#         elif A % i == 0 and B % i == 0:
#             print(i*(A/i)*(B/i))