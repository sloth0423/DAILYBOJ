import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
y = True
count = 0
while y:
    try:
        if x[count]:
            count += 1
    except:
        # break
        y = False
print(count)
# 쉬운 방법 ㅋㅋ
# print(len(x))