import sys

input = lambda: sys.stdin.readline().rstrip()

ls = list()
ls2 = list()
ls3 = list()
for i in range(9):
    x = input().split()
    ls.append([])
    for j in range(9):
        ls[i].append(int(x[j]))
for k in range(9):
    ls2.append(max(ls[k]))
    ls3.append(ls[k].index(max(ls[k])))
print(max(ls2))
z = ls2.index(max(ls2))
print(z + 1, ls3[z] + 1)


# 다른 사람이 적은 코드 하나씩 비교해가면서 현재 최댓값보다 큰 최댓값이 나왔을 때의
# 행과 열을 저장해 놓은 뒤 다 비교하면 출력하게 했다.
# 나는 각 행의 최댓값을 넣은 리스트와
# 각 행의 최댓값이 있는 열을 넣은 리스트를 더 만들었는데 그럴 필요가 없었다.
# N=[list(map(int,input().split())) for _ in range(9)]
# max_value=0
# max_index=(0,0)
# for i in range(9):
#     for j in range(9):
#         if N[i][j] > max_value:
#             max_value = N[i][j]
#             max_index = (i, j)
# print(max_value)
# print(max_index[0] + 1, max_index[1] + 1)