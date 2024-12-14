import sys

input = lambda: sys.stdin.readline().rstrip()

K = int(input())
ls = list()
for _ in range(K):
    n = int(input())
    if not n:
        ls.pop()
    else:
        ls.append(n)
print(sum(ls))

# 다른 사람이 푼 코드
# 이 사람의 코드가 실행시간이 더 짧았는데
# C언어의 파일 입출력을 배울 때 I/O작업은 매우 느리니
# 가능하다면 한 번에 입력을 받아서 한 번에 출력하는게 빠르다고 했는데
# 그 내용이 여기서 적용된 게 아닐까 싶다.
# import sys
#
# stack = list()
# sys.stdin.readline()
# n = list(map(int, sys.stdin.read().rstrip().split('\n')))
#
# for i in n:
#   if (i != 0):
#     stack.append(i)
#   else:
#     stack.pop()
#
# print(sum(stack))