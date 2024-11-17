ls = list(map(int, input().split()))
if max(ls) >= sum(ls) - max(ls):
    print((sum(ls)-max(ls))*2-1)
else:
    print(sum(ls))

# 바꾸기 전 코드
# ls = list(map(int, input().split()))
# a = max(ls)
# b = sum(ls)
# if a >= b - a:
#     print((b - a) * 2 - 1)
# else:
#     print(b)