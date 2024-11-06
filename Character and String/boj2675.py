import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())
for i in range(x):
    y = input()
    a, b = y.split()
    a = int(a)
    count = 0
    for j in range(len(b)):
        print(b[count] * a, end = "")
        # 처음에 했던 방식
        # 그런데 느리다. 위의 방식이 더 빠름
        # for k in range(a):
        #     print(b[count], end = "")
        count += 1
    print("")
