import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ls = list()
for _ in range(N):
    cmd = input()
    if cmd[0] == '1':
        ls.append(int(cmd[2:]))
    if cmd == '2':
        if not ls:
            print(-1)
        else:
            n = ls.pop()
            print(n)
    if cmd == '3':
        print(len(ls))
    if cmd == '4':
        if not ls:
            print(1)
        else:
            print(0)
    if cmd == '5':
        if not ls:
            print(-1)
        else:
            print(ls[-1])

# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N = int(input())
# ls = list()
# for _ in range(N):
#     cmd = input()
#     c = cmd[0]
#     if c == '1':
#         ls.append(int(cmd[2:]))
#     if c == '2':
#         if not ls:
#             print(-1)
#         else:
#             n = ls.pop()
#             print(n)
#     if c == '3':
#         print(len(ls))
#     if c == '4':
#         if not ls:
#             print(1)
#         else:
#             print(0)
#     if c == '5':
#         if not ls:
#             print(-1)
#         else:
#             print(ls[-1])