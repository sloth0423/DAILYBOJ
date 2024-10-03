testCase = input()
for i in range(int(testCase)):
    X = input()
    x1, y1, x2, y2 = X.split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    planetCount = input()
    count = 0
    for j in range(int(planetCount)):
        Y = input()
        cx, cy, r = Y.split()
        cx = int(cx)
        cy = int(cy)
        r = int(r)
        d1 = (((cx - x1)**2)+((cy-y1)**2))**0.5
        d2 = (((cx - x2)**2)+((cy-y2)**2))**0.5
        if d1 < r and d2 < r:
            continue
        if d1 < r:
            count += 1
        elif d2 < r:
            count += 1
    print(count)
