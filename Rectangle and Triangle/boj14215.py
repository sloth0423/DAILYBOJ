ls = list(map(int, input().split()))
if max(ls) >= sum(ls) - max(ls):
    print((sum(ls)-max(ls))*2-1)
else:
    print(sum(ls))