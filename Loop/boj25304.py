x = input()
y = input()
x = int(x)
y = int(y)
total = 0
for i in range (y):
    z = input()
    z1, z2 = z.split()
    z1 = int(z1)
    z2 = int(z2)
    total += z1*z2
if (total == x):
    print("Yes")
else:
    print("No")