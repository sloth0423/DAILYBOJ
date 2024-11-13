x = int(input())
cnt = 1
if x != 1:
    x = x - 1
    while x > (6 * cnt):
            x = x - 6 * (cnt)
            cnt += 1
else:
    cnt = 0
print(cnt + 1)