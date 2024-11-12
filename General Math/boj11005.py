x, y = input().split()
x = int(x)
y = int(y)
ls = list()
while True:
    if x >= y:
        ls.append(x % y)
        x //= y
    else:
        ls.append(x)
        break
z = len(ls)
for i in range(z):
    if ls[z-i-1] < 10:
        print(ls[z-i-1], end = "")
    else:
        print(chr(ls[z-i-1]+55), end = "")