import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())
ls = list()
for _ in range(x):
    ls.append(int(input()))
ls.sort()
for i in range(x):
    print(ls[i])

# 문제가 이걸 물어보는게 아니고 정렬 알고리즘을
# 만들어 보라는 것 같아서 다시 풀어보겠다.
# 사실 아래 코드도 정렬 알고리즘은 아니다.
# import sys
# input = lambda: sys.stdin.readline().rstrip()
# N = int(input())
# ls = list()
# for _ in range(N):
#     ls.append(int(input()))
# for _ in range(N):
#     minNum = min(ls)
#     minIndex = ls.index(minNum)
#     length = len(ls)
#     print(minNum)
#     ls[minIndex] = ls[length-1]
#     ls[length-1] = minNum
#     ls.pop()
# 그래서 다시 만들어 보겠다.
# 일단 생각한 방법 (이게 될지는 모르겠다.)
# 리스트의 양옆에 있는 값들끼리 비교해서(맨 끝의 값들은 둘이 비교함)
# 크면 1을 더한다.(처음 비교하면 최댓값이 2)
# 그리고 그 값들을 기억해 놓았다가
# 한번 더 하고 나온 값들을 이전 값들에 더함
# 그러다가 0 1 1 1 ..... 2 가 나오면 끝나는 거임
# 그런데 문제는 비교한 값들을 정렬 해야한다는 거임 ㅋㅋ;
# 이 방법은 안될 것 같긴 함 ㅠㅠ
# 그리고 비교 횟수가 너무 많다.





