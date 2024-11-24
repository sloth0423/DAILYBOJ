ls = list()
sum = 0
for i in range(5):
    ls.append(int(input()))
for j in range(5):
    sum += ls[j]
ls.sort()
print(sum//5)
print(ls[2])