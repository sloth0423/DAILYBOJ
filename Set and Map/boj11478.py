import sys
input = lambda:sys.stdin.readline().rstrip()

S = input()
s = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s.add(S[i:j])
print(len(s))

# 다른 사람이 푼 코드
# 이 사람은 다른 사람이 푼 코드와 차원이 다르게
# 메모리와 실행시간을 적게 사용하는 코드를 짰다.
# 다른 사람들(나 포함)은 만약 문자열을 n개로 자른다고
# 가정했을 때 같은 문자열이 나올 수 있는 경우는
# 똑같이 n개로 잘랐을 때 밖에 없다는 것을 생각을 안하고
# 그냥 무작정 몇 개로 자르든 set에 넣었는데
# 이 사람은 n개로 자른 것들을 set에 넣고 길이를 재서
# cnt에 추가하고 또 초기화 하고를 n+1개 자른 것을 set에 넣고를 반복했다.
# 그 결과 set의 최대 길이는 S의 길이이며 (다른 사람들은 cnt의 길이)
# 찾을 때도 전체에서 찾는 것이 아닌 일부에서 찾게 되므로
# 메모리와 실행시간을 적게 사용할 수 있게 되었다.

# S = input()
# len_S = len(S)
# cnt = 0
# for i in range(1, len_S + 1):
#     sub_S_set = set()
#     for _ in range(len_S-i+1):
#         sub_S_set.add(S[_:_+i])
#     cnt += len(sub_S_set)
# print(cnt)