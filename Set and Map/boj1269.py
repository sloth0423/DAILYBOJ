import sys

input = lambda:sys.stdin.readline().rstrip()

A, B = map(int, input().split())
ls = list(map(int, input().split()))
ls = ls + list(map(int,input().split()))
ls2 = set(ls)
print(len(ls2)-(len(ls)-len(ls2)))