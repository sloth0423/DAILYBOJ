def printStar(N):
    if N == 1:
        return ["***","* *","***"]
    prev = printStar(N-1)
    size = len(prev)
    ls = []
    for row in prev:
        ls.append(row*3)
    for row in prev:
        ls.append(row+" "*size+row)
    for row in prev:
        ls.append(row*3)
    return ls

N = int(input())
n = 0
for i in range(1, 9):
    if 3 ** i == N:
        n = i
        break
result = printStar(n)
print("\n".join(result))
