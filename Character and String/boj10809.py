import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
ls = list()
for i in range(26):
    ls.append(-1)
for j in range(len(x)):
    for k in range(26):
        if x[j] == chr(97+k):
            if ls[k] == -1:
                ls[k] = j
for l in range(26):
    print(ls[l], end = " ")

