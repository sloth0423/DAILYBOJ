x = input()
ls = list()
for i in range(len(x)):
    ls.append(int(x[i]))
ls.sort()
for word in reversed(ls):
    print(word, end = '')