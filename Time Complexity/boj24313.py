import sys
input = lambda: sys.stdin.readline().rstrip()

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

while True:
    if a0 > 0:
        if (a1*n0)+a0 > c*n0:
            print(0)
            break
        else:
            if a1 < c:
                print(1)
                break
            else:
                print(0)
                break
    elif a0 < 0:
        if (a1*n0)+a0 > c*n0:
            print(0)
            break
        else:
            if a1 > c:
                print(0)
                break
            else:
                print(1)
                break
