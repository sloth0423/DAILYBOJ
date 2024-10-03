X = input()
for i in range(0, int(X)):
    x1, y1, r1, x2, y2, r2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    r1 = int(r1)
    r2 = int(r2)
    if r2 > r1:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print("-1")
    elif d > r1 + r2:
        print("0")
    elif d == r1 + r2:
        print("1")
    elif d + r2 < r1:
        print("0")
    elif d + r2 == r1:
        print("1")
    else:
        print("2")


