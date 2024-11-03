import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = 9
ls = list()
for i in range(testCase):
    x = input()
    x = int(x)
    ls.append(x)
maxNum = ls[0]
count = 0
for j in range(testCase):
    if maxNum <= ls[j]:
        maxNum = ls[j]
for k in range(testCase):
    if ls[k] == maxNum:
        break
print(maxNum)
print(k+1)
# 이렇게도 해봄
# print(max(ls))
# print(ls.index(max(ls))+1)