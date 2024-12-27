import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
s = set()
try:
    while True:
        i = input()
        if i == "":
            raise EOFError
        else:
            a, b = i.split()
        if a == "ChongChong" or b == "ChongChong":
            s.add(a)
            s.add(b)
        if a in s:
            s.add(b)
        if b in s:
            s.add(a)
except EOFError:
    print(len(s))
