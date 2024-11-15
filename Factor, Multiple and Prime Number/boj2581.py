x = int(input())
y = int(input())

sumNum = 0
minNum = 0
for i in range(x, y+1):
    cnt = 0
    if i != 1:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            if sumNum == 0:
                minNum += i
            sumNum += i
if sumNum == 0:
    print("-1")
else:
    print(sumNum)
    print(minNum)

# 다른 사람이 푼 코드
# 어차피 2를 제외한 짝수라면 소수일 수 없기 때문에
# for y in range(5, limit + 1, 2):
# 에서 뒤에 2를 추가하여 홀수만 나오게 했다.
# import math
#
# m = int(input())
# n = int(input())
#
# num_list = []
#
# for i in range(m, n + 1):
#     if i == 2 or i == 3:
#         num_list.append(i)
#     elif i > 3 and i % 2 != 0 and i % 3 != 0:
#         limit = int(math.sqrt(i))
#         check = True
#         for y in range(5, limit + 1, 2):
#             if i % y == 0:
#                 check = False
#         if check:
#             num_list.append(i)
#
# if num_list:
#     print(sum(num_list))
#     print(min(num_list))
# else:
#     print(-1)