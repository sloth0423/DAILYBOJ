import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
x = int(x)

for i in range (1, x+1):
    for j in range (x-i):
        print(" ", end = "")
    for k in range (1, i+1):
        print("*", end = "")
    print("")