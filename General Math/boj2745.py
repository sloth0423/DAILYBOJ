x, y = input().split()
y = int(y)
z = len(x)
rslt = 0
for i in range(z):
    if ord(x[z-i-1]) < 65:
        rslt += (int(x[z-i-1]))*(y**i)
    else:
        rslt += (ord(x[z-i-1])-55)*(y**i)
print(rslt)

# 다른 사람이 푼 방법
# int() 함수의 첫번째 매개변수인 문자열을
# 두번째 매개변수의 진법 수로 바꿀 수 있다.
# 10진법이 넘어간다면 자동으로 A-Z로 10~35를 표현한다고 한다.
# 거의 이 문제를 풀기 위해 만든 함수인 듯 ㄷㄷ;

# n, b = map(str, input().split())
# print(int(n, int(b)))