a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

ls = [a, c, e]
ls2 = [b, d, f]

for i in ls:
    if ls.count(i) == 1:
        print(i, end = " ")
for j in ls2:
    if ls2.count(j) == 1:
        print(j)
