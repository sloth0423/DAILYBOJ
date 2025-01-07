import sys

input = sys.stdin.read

def backtrack(sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        if i not in sequence:
            backtrack(sequence + [i])

N, M = map(int, input().split())
backtrack([])