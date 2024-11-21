import sys
input = lambda:sys.stdin.readline().rstrip()
W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B',
     'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W',
     'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
N, M = map(int, input().split())
ls = list()
for i in range(N):
    ls.append(list(map(str, input())))
ls3 = set()
for j in range(N - 7):
    for k in range(M - 7):
        ls2 = []
        for l in range(8):
            for m in range(8):
                ls2.append(ls[j+l][k+m])
        WNum, BNum = 0, 0
        for n in range(64):
            if ls2[n] != W[n]:
                WNum += 1
            if ls2[n] != B[n]:
                BNum += 1
        ls3.add(min(WNum, BNum))
print(min(ls3))
