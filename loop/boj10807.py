import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
x = int(x)

y = input()
y = y.split()
z = input()
z = int(z)
count = 0
for i in range(x):
    if int(y[i]) == z:
        count += 1
print(count)
# python에는 ++, -- 가 없다고 한다.