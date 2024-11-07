import sys

input = lambda: sys.stdin.readline().rstrip()

while(1):
    try:
        x = input()
        print(x)
        if x == "":
            raise(EOFError)
    except:
        break

