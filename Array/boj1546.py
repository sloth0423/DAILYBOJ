import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
x = int(x)
y = input()
y = y.split()
ls = list()
ls2 = list()
sum = 0
for i in range(x):
    ls.append(int(y[i]))
for j in range(x):
    ls2.append((ls[j]/max(ls))*100)
for k in range(x):
    sum += ls2[k]
print(sum/x)