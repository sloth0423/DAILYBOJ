N = int(input())
cnt = 0
num = 0
found = False
while not found:
    num += 1
    if '666' in str(num):
        cnt += 1
    if N == cnt:
        found = True
print(num)
# 다른 사람이 푼 코드
# 이 사람은 나랑 거의 비슷하게 풀었는데
# 일단 666까지는 666이 들어간 숫자가 나올 수가 없기 때문에
#  처음에 숫자를 666부터 시작했고
# 함수를 만든 뒤 함수를 사용해서 풀었는데
# 이 방법이 더 빨랐다.(내 방식도 666부터 시작하게 만들고 비교해 보았음에도)
# 앞으로 함수를 만들어서 풀어야겠다.

# def find_end_number(N):
#     count = 0
#     num = 666
#
#     while True:
#         if '666' in str(num):
#             count += 1
#             if count == N:
#                 return num
#         num += 1
#
#
# N = int(input())
# print(find_end_number(N))