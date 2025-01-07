def dfs(start, depth):
    if depth == m:
        print(*result)
        return
    for i in range(start, n + 1):
        result.append(i)
        dfs(i + 1, depth + 1)
        result.pop()


n, m = map(int, input().split())

result = []
dfs(1, 0)