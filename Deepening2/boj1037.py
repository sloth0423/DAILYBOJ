import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
ls = sorted(list(map(int, input().split())))
print(ls[0] * ls[-1])

# 처음에 푼 방법
# 생각해보니 정렬된 배열에서 최솟값과 최댓값을 찾는게 빠르다.
# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# T = int(input())
# ls = list(map(int, input().split()))
# print(max(ls)*min(ls))
