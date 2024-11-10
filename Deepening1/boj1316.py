import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = int(input())
countNum = 0
for i in range(testCase):
    word = input()
    result = [word[0]]
    for char in word[1:]:
        if result[-1] != char:
            result.append(char)
    word1 = "".join(result)
    ls2 = set(word1)
    if len(word1) == len(ls2):
        countNum += 1
print(countNum)

# ChatGPT가 알려준 문자열에 연속으로 중복된 문자를 빼주는 코드
# result =  []
    # for char in word:
    #     if not result or result[-1] != char:
    #         result.append(char)
    # word1 = "".join(result)
# 처음에 짠 바뀐 문자열에 문자가 여러번 들어있으면 그 문자를 리스트에 넣고,
# ls가 비어 있다면 countNum을 1 증가시키는 코드
#     ls = []
#     for char in word1:
#         if word1.count(char) != 1:
#             ls.append(char)
#     if not ls:
#         countNum += 1
# print(countNum)

# 두번째로 짠 바뀐 문자열을 set에 넣은 뒤 다시 바뀐 문자열과 비교하여
# 길이가 같으면 countNum이 1 증가하는 코드
#     ls2 = set()
#     for char in word1:
#         ls2.add(char)
#     if len(word1) == len(ls2):
#         countNum += 1
# print(countNum)