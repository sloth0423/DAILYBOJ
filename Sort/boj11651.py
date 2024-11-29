import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
ls = [input() for _ in range(N)]
ls.sort(key = lambda x: int(x.split()[0]))
ls.sort(key = lambda x: int(x.split()[1]))
print("\n".join(ls))


# 이전 문제에서 실행시간이 압도적으로 빠른 다른 사람의 풀이를 본 뒤
# 비슷한 문제를 푼 것이기 때문에 나중에 다시 봐야할 것 같다.
