M = int(input())
num = M - len(str(M)) * 9
result = 0
for i in range(max(1, num), M):
    sumNum = 0
    num2 = str(i)
    for j in num2:
        sumNum += int(j)
    sumNum += i
    if sumNum == M:
        result = i
        break
if result == 0:
    print(0)
else:
    print(result)
# 푼 뒤 다른 사람의 풀이를 봤는데
# 아예 모든 케이스를 볼 필요가 없이
# 어차피 M의 자릿수 그러니까 M이 9783이라면
# N은 9783 - (M의 자릿수의 개수? * 9) 보다 작을 수가 없다.
# 숫자는 9까지만 있기 때문이다.
# 그러나 M이 18보다 작으면 내가 사용하는 방법을 쓸 수가 없다.
# 그래서 다른 사람들은 18보다 작을 때에는 모든 케이스를 돌려보기 위해 max()를 사용했다.
# 이 사실을 알기 전 코드

# M = int(input())
# result = 0
# for i in range (1, M+1):
#     sumNum = 0
#     x = str(i)
#     for j in range(len(x)):
#         sumNum += int(x[j])
#     sumNum += i
#     if sumNum == M:
#         result = i
#         break
# if result == 0:
#     print(0)
# else:
#     print(i)


