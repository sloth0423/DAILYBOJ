import sys

input = lambda: sys.stdin.readline().rstrip()

# 어제인가 이틀 전에 배운 reversed()랑 "".join()을 사용한 코드
x = input()
y = "".join(reversed(x))
if x == y:
    print(1)
else:
    print(0)

# 처음에 짠 코드
# testCase = len(x)//2
# judge = True
# for i in range(testCase):
#     if x[i] != x[-(1+i)]:
#         judge = False
# if judge == True:
#     print(1)
# else:
#     print(0)

