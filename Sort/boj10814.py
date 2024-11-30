import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
ls = [input() for _ in range(N)]
ls.sort(key = lambda x: int(x.split()[0]))
print("\n".join(ls))