import sys
input = lambda: sys.stdin.readline().rstrip()

ans = []
while True:
    sen = input()
    ls = []
    n = ''
    flag = 1
    if sen == '.':
        break
    for i in sen:
        if i == '(' or i == '[':
            ls.append(i)
        elif i == ')':
            if len(ls) == 0:
                flag = 0
                break
            n = ls.pop()
            if n != '(':
                flag = 0
                break
        elif i == ']':
            if len(ls) == 0:
                flag = 0
                break
            n = ls.pop()
            if n != '[':
                flag = 0
                break
    if flag and not ls:
        ans.append("yes")
    else:
        ans.append("no")
print("\n".join(ans))


