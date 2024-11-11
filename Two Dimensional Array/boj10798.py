import sys

input = lambda: sys.stdin.readline().rstrip()

ls = list()
ls2 = list()
for i in range(5):
    x = input()
    ls.append([])
    for j in range(len(x)):
        ls[i].append(x[j])
for k in range(5):
    ls2.append(len(ls[k]))
y = max(ls2)
for l in range(5):
    for m in range(y-len(ls[l])):
        ls[l].append('*')
for n in range(y):
    for o in range(5):
        if ls[o][n] != '*':
            print(ls[o][n], end = "")

# 다른 사람이 적은 코드
# index를 벗어난 값이 나오지 않게 하기 위해 if len(words[i]) > n: 이라는
# 조건을 추가해주었다.
# 나는 읽게하다가 index를 벗어난 값이 나왔을 때 처리를 어떻게 해야 할지 몰라
# 길이가 모자란 행에 *를 추가하여 모든 행이 길이를 같게 만들어 준 뒤 *가 나오면
# 출력하지 않게 하였다. 근데 그럴 필요가 없었다.
# words = []
#
# for i in range(5):
#     words.append(input())
#
# for n in range(15):
#     for i in range(5):
#         if len(words[i]) > n:
#             print(words[i][n], end='')