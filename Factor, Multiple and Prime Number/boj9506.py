import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    ls = list()
    testNum = int(input())
    if testNum == -1:
        break
    for i in range(1, testNum):
        if testNum % i == 0:
            ls.append(i)
    if testNum == sum(ls):
        print(f"{testNum} = {' + '.join(map(str, ls))}")
        # print(f"{testNum} = {ls[0]}", end = "")
        # for j in range(1, len(ls)):
        #     print(f" + {ls[j]}", end = "")
        # print("")
    else:
        print(f"{testNum} is NOT perfect.")
# 다른 사람이 푼 코드
# x를 a로 나누면 b가 나오는데 a도 약수이고 b도 약수이므로
# 제곱근까지만 계산해서 둘 다 넣어줬다.
# 그리고 x를 뺀 후 더했다.
# while True:
#     x = int(input())
#     divisor_set = set()
#
#     if x == -1:
#         break
#     #int(x**0.5) + 1 --> x의 제곱근까지의 범위
#     for divisor in range(1, int(x**0.5) + 1):
#         if x % divisor == 0:
#             divisor_set |= {divisor, x // divisor}
#     divisor_set = list(divisor_set)
#     divisor_set.remove(x)
#     divisor_set.sort()
#     sum_num = sum(divisor_set)
#
#     if sum_num == x:
#         print(f'{x} = {" + ".join(map(str, divisor_set))}')
#     else:
#         print(f'{x} is NOT perfect.')