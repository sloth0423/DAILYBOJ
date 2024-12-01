import  sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
ls= set(map(int, input().split()))
M = int(input())
ls2 = list(map(int, input().split()))
for i in ls2:
    if i in ls:
        print(1, end = " ")
    else:
        print(0, end = " ")

# 나는 그냥 set이 list에서 중복되는 값만 제거해주는 자료형으로 알고 있었는데
# 원소를 해시 테이블을 기반으로 저장하기 때문에 원소를 검색할 때 거의 상수시간에
# 찾아낼 수 있다고 한다.
# 어쩐지 아까 ls를 set이 아닌 list로 풀 때 시간이 오래걸렸는데
# 상술한 이유 때문이었다.

# 세번째로 푼 방법
# import  sys
# input = lambda:sys.stdin.readline().rstrip()
#
# N = int(input())
# ls= list(map(int, input().split()))
# M = int(input())
# ls2 = list(map(int, input().split()))
# for i in ls2:
#     if i in ls:
#         print(1, end = " ")
#     else:
#         print(0, end = " ")

# 두번째로 푼 방법
# for i in range(M):
#     for j in range(N):
#         if ls2[i] == ls[j]:
#             print(1, end = " ")
#             break
#     if ls2[i] == ls[j]:
#         continue
#     print(0, end = " ")

# 처음에 푼 방법
# for i in range(M):
#     if ls.count(ls2[i]) == 0:
#         print(0, end = " ")
#     else:
#         print(1, end = " ")