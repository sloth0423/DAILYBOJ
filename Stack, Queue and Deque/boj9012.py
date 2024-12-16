import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    word = input()
    n = 0
    for i in word:
        if i == '(':
            n += 1
        else:
            n -= 1
            if n < 0:
                n = 1
                break
    if n:
        print("NO")
    else:
        print("YES")

# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# T = int(input())
#
# for _ in range(T):
#     word = input()
#     ls = []
#     for i in word:
#         try:
#             if i == '(':
#                 ls.append(i)
#             elif i == ')':
#                 ls.pop()
#         except:
#             print("NO")
#             ls.append(-1)
#             break
#     if ls == [-1]:
#         continue
#     elif ls:
#         print("NO")
#     else:
#         print("YES")

