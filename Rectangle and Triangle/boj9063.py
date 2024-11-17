import sys

input = sys.stdin.readline

n = int(input())

ls = set()
ls2 = set()
for i in range(n):
    x, y = map(int,input().split())
    ls.add(x)
    ls2.add(y)
print((max(ls)-min(ls))*(max(ls2)-min(ls2)))

# set으로 만들면 더 빠르고 메모리도 아낄 수 있음
# 왜인지 모르겠지만 다른 사람 코드와 비교해 봤을 때
# 변수의 글자가 대문자인 것보다 소문자인 것이 빨랐으며
# for _ in range(): 보다
# for i in range(): 가 더 빨랐다.