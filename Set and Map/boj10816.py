import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
dic = {}
ls = list(map(int, input().split()))
for k in range(N):
    i = ls[k]
    if not i in dic:
        dic[i] = 1
    else:
        dic[i] += 1
M = int(input())
ls1 = list(map(int, input().split()))
ls2 = list()
for l in range(M):
    j = ls1[l]
    if j in dic:
        ls2.append(str(dic[j]))
    else:
        ls2.append('0')
print(" ".join(ls2))

# 다른 사람이 푼 방법
# Counter함수를 import해서 풀었다.
# Counter함수는 문자열이나 배열같은 나열 가능한 객체?가 들어오면
# 문자열 혹은 배열에 각 요소가 몇 개가 들어있는지 알려주는 함수이다.
# 맨 아래 문장은 data[3](상근이가 몇 장 가지고 있는지 세야하는 카드들)에
# 각 요소가 N(상근이가 가지고 있는 카드들에 Counter함수를 사용한 객체(딕셔너리 인듯))에
# 있다면 N에 요소가 key인 value값을 적는 문장이다.
#
# from collections import Counter
# import sys
# data = sys.stdin.readlines()
# N = Counter(data[1].split())
# print(' '.join(str(N[x]) if x in N else '0' for x in data[3].split()))