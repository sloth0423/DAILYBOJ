import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ls = [0]*10000
for _ in range(N):
    num = int(input()) - 1
    ls[num] += 1
for k in range(10000):
        for _ in range(ls[k]):
            print(k + 1)


# 아래의 코드는 chat gpt에게 계수 정렬(counting sort)에 대해
# 물어보니 짜준 코드를 문제에 맞게 살짝 변경한 코드이다.
# import sys
# input = lambda: sys.stdin.readline().rstrip()
# def counting_sort(input):
#     n = len(input)      # 입력 배열의 크기
#     k = max(input)      # 입력 배열의 최댓값
#     counts = [0] * (k + 1)  # k+1 크기의 counts 배열 생성
#
#     # counts 배열에 각 원소의 개수 저장
#     for num in input:
#         counts[num] += 1
#
#     # counts 배열을 누적 합으로 업데이트
#     for i in range(1, len(counts)):
#         counts[i] += counts[i - 1]
#
#     ans = [0] * n  # n 크기의 결과 배열 생성
#
#     # 입력 배열의 각 원소를 정렬된 위치에 삽입
#     for num in input:
#         ans[counts[num] - 1] = num
#         counts[num] -= 1
#
#     return ans
# N = int(input())
# ls = list()
# ls2 = list()
# for _ in range(N):
#     ls.append(int(input()))
# ls2 = counting_sort(ls)
# for i in range(N):
#     print(ls2[i])