x, y, z = map(int,input().split())

a = z - x
b = a % (x - y)
c = a//(x - y)
if b == 0:
    print(c + 1)
else:
    print(c + 1 + 1)
