import sys
input = lambda:sys.stdin.readline().rstrip()
dic = {}
dic2 = {}
N ,M = map(int, input().split())
for i in range(1, N+1):
    j = input()
    dic[j] = i
    dic2[i] = j
ans = []
for _ in range(M):
    que = input()
    if que in dic:
        ans.append(str(dic[que]))
    elif int(que) in dic2:
        ans.append(dic2[int(que)])
print("\n".join(ans))

# 다른 사람이 푼 코드
# 나는 문자열을 key로 하는 딕셔너리와
# 숫자를 key로 하는 딕셔너리 두개를 만들었는데
# 사실 그럴 필요가 없었다.
# 문자열을 key로 하는 딕셔너리를 하나 만들고
# 포켓몬의 이름을 들어온 순서대로 저장하는 리스트를 하나 더 만들면 됐다.
# 그 이유는 리스트의 인덱스에 1을 더하면 숫자가 되고,
# 리스트(배열)에서 인덱스를 통해 값을 찾는 것은 빠르기 때문이다.
# 해당 질문이 숫자인지 아닌지 판별하는 과정도 나와 달랐다.
# 그래서 맨 밑에 내가 처음에 푼 코드를 좀 더 정리해서 적어보겠다.

# import sys
#
# input = sys.stdin.read
# data = input().splitlines()
#
# # 첫 줄의 N과 M 받기
# N, M = map(int, data[0].split())
#
# # 도감을 저장할 딕셔너리
# name_to_num = {}
# num_to_name = []
#
# # N개의 포켓몬 이름 입력 처리
# for i in range(1, N + 1):
#     pokemon = data[i]
#     name_to_num[pokemon] = i
#     num_to_name.append(pokemon)
#
# # M개의 질문 처리
# output = []
# for i in range(N + 1, N + 1 + M):
#     query = data[i]
#     if query.isdigit():
#         output.append(num_to_name[int(query) - 1])
#     else:
#         output.append(str(name_to_num[query]))
#
# # 결과 출력
# sys.stdout.write("\n".join(output) + "\n")

# 고친 코드
# import sys
# input = lambda:sys.stdin.readline().rstrip()
# dic = {}
# dic2 = {}
# N ,M = map(int, input().split())
# for i in range(1, N+1):
#     j = input()
#     dic[j] = i
#     dic2[i] = j
# ans = []
# for _ in range(M):
#     que = input()
#     if que.isdigit():
#         ans.append(dic2[int(que)])
#     else:
#         ans.append(str(dic[que]))
# print("\n".join(ans))