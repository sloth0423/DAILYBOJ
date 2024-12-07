import sys
input = lambda:sys.stdin.readline().rstrip()
A, B = map(int, input().split())
C, D = map(int, input().split())
E, F = (A*D)+(C*B), B*D
e, f = E, F
while e % f != 0:
    r = e % f
    e = f
    f = r
print(f"{E//f} {F//f}")