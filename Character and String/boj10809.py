import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
ls = list()
for i in range(26):
    ls.append(-1)
for j in range(len(x)):
    for k in range(26):
        if x[j] == chr(97+k):
            if ls[k] == -1:
                ls[k] = j
for l in range(26):
    print(ls[l], end = " ")

# 다른 사람이 한 코드
# s = input()
# abc = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in abc:
#     if i in s:
#         print(s.index(i), end =' ')
#     else:
#         print('-1', end = ' ')
'''
내 코드는 리스트를 만들어 놓은 후 입력의 j번째에 해당하는
알파벳의 번호(k)를 찾은 뒤 리스트의 k번째에 j를 넣는다.
이 사람의 코드는 리스트도 필요없고 알파벳 순으로 
있는지 없는지 찾아내면서 있으면 index()를 이용하여 출력
'''