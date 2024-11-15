# 다른 사람이 만든 함수
# 함수로 만드니까 cnt(count)변수를 안 만들어도 됨
# 반환값이 cnt 역할을 함
def is_Prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

x = int(input())
if x != 1:
    div = 2
    while not is_Prime(x):
        if is_Prime(div) and x % div == 0:
            x //= div
            print(div)
        else:
            div += 1
    print(x)

# 다른 사람이 푼 코드
# 생각해보니 처음에 2로 계속 나누고 나눠지는게 없으면
# 제수를 1씩 계속 키우면서 또 나누고 하다보면
# 자연스럽게 제수가 소수일 때만 나눠진다.
# 그러므로 내 코드에서 is_Prime은 한번만 사용하면 되는 것이었다.
# 그리고 이 사람의 대단한 점은 계속 제수를 1씩 더해가면서 나누다가
# 제수가 피제수의 제곱근보다 커지면
# 자연스럽게 피제수가 소수가 된다는 것을 이용했다는 것이다.
#
# n = int(input())
# i = 2
# while n > 1:
#     if (n%i) == 0:
#         print(i)
#         n = n // i
#     else:
#         i += 1
#         if i > int(n**0.5):
#             i = n