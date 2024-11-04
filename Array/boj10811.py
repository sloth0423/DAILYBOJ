import sys

input = lambda: sys.stdin.readline().rstrip()

ls = list()
x, y = map(int, input().split())
for i in range(x):
    ls.append(i+1)
for j in range(y):
    num1, num2 = map(int, input().split())
    count=(num2-num1+1)//2
    for k in range(count):
        num3 = num1 + num2
        if (num3 % 2 == 0):
            avr  = num3//2
            ls[avr-k-2],ls[avr+k] = ls[avr+k],ls[avr-k-2]
        else:
            avr = num3 / 2
            ls[int(avr-k-1.5)],ls[int(avr+k-0.5)] = ls[int(avr+k-0.5)],ls[int(avr-k-1.5)]
for l in range(x):
    print(ls[l], end = " ")
