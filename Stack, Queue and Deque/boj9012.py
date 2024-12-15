import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    word = input()
    ls = []
    for i in word:
        try:
            if i == '(':
                ls.append(i)
            elif i == ')':
                ls.pop()
        except:
            print("NO")
            ls.append(-1)
            break
    if ls == [-1]:
        continue
    elif ls:
        print("NO")
    else:
        print("YES")

