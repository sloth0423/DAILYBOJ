import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
x = int(x)
y = input()
y = y.split()
maxNum = int(y[0])
minNum = int(y[0])
for i in range(x-1):
    if maxNum <= int(y[i+1]):
        maxNum = int(y[i+1])
for j in range(x-1):
    if minNum >= int(y[j+1]):
        minNum = int(y[j+1])
print(f"{minNum} {maxNum}")
# 이렇게도 가능
# ls = []
# for i in range(x):
#     ls.append(int(y[i]))
# print(f"{min(ls)} {max(ls)}")