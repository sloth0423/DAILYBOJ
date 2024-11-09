import sys

input =lambda: sys.stdin.readline().rstrip()

x = input()

ls = list()
for _ in range(26):
    ls.append(0)
for i in range(len(x)):
    if ord(x[i]) < 97:
        ls[ord(x[i])-65] += 1
    else:
        ls[ord(x[i])-97] += 1
a = max(ls)
b = ls.index(a)
ls[b] = 0
c = max(ls)
if a == c:
    print('?')
else:
    print(chr(b+65))

# 다른 사람이 푼 코드 upper() 함수와
# count()를 사용하여 빠르게 풀었다.
# word = input().upper()
# result = []
# for i in range(65, 91):
#     result.append(word.count(chr(i)))
# if result.count(max(result)) > 1:
#     print("?")
# else:
#     print(chr(result.index(max(result))+65))