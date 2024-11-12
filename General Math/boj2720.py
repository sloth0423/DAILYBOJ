import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = int(input())
for _ in range(testCase):
    change = int(input())
    changeQ = change // 25
    change -= changeQ * 25
    changeD = change // 10
    change -= changeD * 10
    changeN = change // 5
    change -= changeN * 5
    changeP = change // 1
    change -= changeP * 1
    print(f"{changeQ} {changeD} {changeN} {changeP}")

# 생각해보니 (몫 * 제수)를 피제수(혹은 피연산자)에서 뺀 것이 나머지였다.
# 그래서 changeQ -= changeQ*25는
# changeQ %= 25 라고 적어도 됐다.
# 나눗셈에서 나눠지는 수를 피제수(혹은 피연산자)라고 하고,
# 나누는 수를 제수라고 한다고 한다.
# 초등학교 때 배웠던 거 같은데 까먹음;;