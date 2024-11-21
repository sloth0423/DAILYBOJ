a, b, c, d, e, f = map(int, input().split())
x = 0
y = 0
for i in range(-999,1000):
    for j in range(-999,1000):
        if a * i + b * j == c and d * i + e * j == f:
            x = i
            y = j
            break
print(x, y)

# # 사실 이 문제를 풀 때 대입법을 먼저 생각해냈다.
# 하지만 a,b,c,d,e,f 중에서 0이 나올 때의 경우에
# 코드를 어떻게 짜야할지가 조금 난감했다.
# 그래서 그냥 단원 이름도 브루트 포스이길래 위와 같이 코드를 썻는데
# 다른 사람이 푼 코드에 소거법을 이용한 방법이 있었다.
# 계속 반례를 생각해봐도 나오지 않았다.
# 결론: 대단한 것 같다.
# (왜 자꾸 일기가 되어가는 것 같지...)

# a, b, c, d, e, f = map(int, input().split())
#
# # ax + by = c
# # dx + ey = f
# x = 0
# y = 0
#
# if a == 0:
#     y = int(c / b)
#     x = int((f - e * y) / d)
# elif b == 0:
#     x = int(c / a)
#     y = int((f - d * x) / e)
# else:
# # if a and b and c and d:
#     y = int((c * d - f * a) / (b * d - e * a))
#     x = int((c - b * y) / a)
#
#
#
# print(x, y)