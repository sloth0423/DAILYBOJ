import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
rslt = 0

while True:
    try:
        s = set()
        while True:
            i = input()
            if i == 'ENTER':
                rslt += len(s)
                break
            elif i == "":
                raise EOFError
            else:
                s.add(i)
    except EOFError:
        rslt += len(s)
        print(rslt)
        break
