import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
y = len(x)

z = (x.count('c=') + x.count('c-') + x.count('d-') + x.count('dz=') \
     + x.count('lj')+ x.count('nj')+ x.count('s=') + x.count('z='))

print(y-z)

# 다른 사람이 푼 코드
# replace('a문자열','b문자열') 함수: 문자열에서 a문자열을 b문자열로 바꿔줌
# s = input()
# s = s.replace('c=','1').replace('c-','2').replace('dz=','3').replace('d-','4').replace('lj','5').replace('nj','6').replace('s=','7').replace('z=','8')
# print(len(s))