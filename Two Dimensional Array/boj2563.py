import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())

set1 = set()
for _ in range(x):
    y, z = map(int, input().split())
    for k in range(10):
        for j in range(10):
            set1.add(((z+k)*100)+y+j)
print(len(set1))

# 처음에 푼 방법
# 0 부터 9999까지의 리스트(ls)를 만든 후
# 색종이를 올렸을 때 가리는 점들을 리스트(ls2)에 넣고
# ls2에 있는 점이 ls1에 있으면 지우고 없으면 넘어가게 한 후
# 10000에서 ls의 길이를 빼줬다.
# 하지만 그냥 set에 넣으면 자동으로 겹치는 요소를 지워주기 때문에
# 그럴 필요가 없었다.
# ls = list()
# for i in range(10000):
#     ls.append(i)
# for _ in range(x):
#     ls2 = []
#     y, z = map(int, input().split())
#     for k in range(10):
#         for j in range(10):
#             ls2.append(((z+k)*100)+y+j)
#     for l in range(len(ls2)):
#         if ls2[l] in ls:
#             ls.remove(ls2[l])
# print(10000-len(ls))


