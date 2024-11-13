x = int(input())
y = 0
n = 2
for i in range(1, x + 1):
    n = (2 * n) - 1 # n + (n - 1)
    y = n ** 2
print(y)