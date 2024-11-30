# import sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N = int(input())
# ls = list(map(int,input().split()))
# ls2 = sorted(set(ls))
# n = len(ls2)
# D = {}
# for i in range(n):
#     D[ls2[i]] = i
# for j in range(N):
#     print(D[ls[j]], end = " ")


# 아래는 내가 처음에 풀었던 코드이다.
# for문 안에 index()가 들어가니
# 탐색하는데 시간이 너무 오래걸리는지 자꾸 시간 초과가 나와서
# chat gpt에게 물어보니 딕셔너리를 이용하면 해시 함수를 이용하는
# 자료구조인 해시 테이블을 사용하여 빠르게 찾을 수 있다고 해서
# 딕셔너리를 이용해 만들어 보았다.

# import sys
# input = lambda:sys.stdin.readline().rstrip()
# N = int(input())
# ls = list(map(int,input().split()))
# ls2 = list(set(ls))
# ls2.sort()
# for i in range(N):
#     print(ls2.index(ls[i]) , end = " ")
