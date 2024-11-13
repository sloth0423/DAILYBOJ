x = int(input())
y = 1
while x > y:
    x -= y
    y += 1
if y % 2 == 0:
    print(f"{x}/{y+1-x}")
else:
    print(f"{y+1-x}/{x}")