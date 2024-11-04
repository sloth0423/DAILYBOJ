import sys

input = lambda: sys.stdin.readline().rstrip()

ls = list()
ls2 = list()
setIsGood = set()
for i in range(10):
    x = input()
    x = int(x)
    ls.append(x)
for j in range(10):
    ls2.append(ls[j] % 42)
for k in range(10):
    setIsGood.add(ls2[k])
print(len(setIsGood))