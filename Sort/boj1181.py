import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())

ls = set(input() for _ in range(N))
ls = list(ls)
ls.sort()
ls.sort(key = lambda x: len(x))
print("\n".join(ls))