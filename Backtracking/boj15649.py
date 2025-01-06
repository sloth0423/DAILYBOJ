import sys

input = sys.stdin.read


def backtrack(sequence):
    if len(sequence) == M:  # 길이가 M인 순열이 완성되면 출력
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        if i not in sequence:  # 중복 방지
            backtrack(sequence + [i])  # 새로운 수를 추가하여 재귀 호출


# N과 M을 입력받음
N, M = map(int, input().split())
backtrack([])