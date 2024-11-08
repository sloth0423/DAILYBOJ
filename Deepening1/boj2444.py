import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())

for i in range(x):
    print(" "* (x-i-1), end = "")
    print("*"* ((2*(i+1)-1)))
for j in range(x-1):
    print(" "*(j+1), end = "")
    print("*"* ((2*(x-j-1))-1))