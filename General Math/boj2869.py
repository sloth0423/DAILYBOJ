x, y, z = map(int,input().split())

a = z - x
b = a % (x - y)
c = a // (x - y)
if b == 0:
    print(c + 1)
else:
    print(c + 1 + 1)

# 다른 사람이 푼 방법
# 나는 마지막 날에 도착하면 끝이므로
# 올라가는 것을 빼고 생각했다.
# 이 사람은
# A는 무조건 B보다 크고,
# B + (A-B로 나눈 나머지)는 무조건 A보다 작으므로
# B를 먼저 빼놓고 풀었다.
#
# A, B, V = map(int, input().split())
#
# x = (V-B)/(A-B)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)