x = int(input())
y = int(input())
z = int(input())


if x + y + z != 180:
    print("Error")
elif x == y and y == z:
    print("Equilateral")
elif x != y and y != z and x != z:
    print("Scalene")
else:
    print("Isosceles")