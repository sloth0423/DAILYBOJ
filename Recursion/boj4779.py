def cantor(N):
    if N == 0:
        return "-"
    prev = cantor(N-1)
    return prev+ " " * len(prev) + prev

while True:
    try:
        N = int(input())
        print(cantor(N))
    except EOFError:
        break