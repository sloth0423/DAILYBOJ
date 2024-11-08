import sys

input = lambda: sys.stdin.readline().rstrip()

ls = [1,1,2,2,2,8]
ls2 = list()
x = input().split()
for i in range(len(ls)):
    ls2.append(int(ls[i]) - int(x[i]))

for j in range(len(ls2)):
    print(ls2[j],end = " ")
