import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
dic = {}
ls = list()
for _ in range(n):
    p, l  = input().split()
    dic[p] = l
for value in dic:
    if dic[value] == "enter":
        ls.append(value)
ls.sort()
print("\n".join(reversed(ls)))

# 다른 사람이 푼 방식
# 이 방법은 dictionary로 풀지 않고 set만을 이용하여 풀었다.
# 만약 set에 사람 이름이 없으면 출근하는 것이고,(set에 추가)
# 있으면 퇴근하는 것이다.(set에서 삭제)
# 마지막에 set에 있으면 회사 안에 있는 것이므로
# sorted(set, reverse = True)를 이용해 사전의 역순으로 바꿔준 뒤
# join()을 이용하여 출력해주었다.
# import sys
# EL_set = set()
# N = int(sys.stdin.readline().rstrip())
# for _ in range(N):
#     N,E_L = sys.stdin.readline().split()
#     if N in EL_set:
#         EL_set.remove(N)
#     else:
#         EL_set.add(N)
# setTOlst = sorted(EL_set,reverse= True)
# print('\n'.join(setTOlst))