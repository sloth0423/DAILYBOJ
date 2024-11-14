x, y = map(int, input().split())
cnt = 0 # 0이 몇번 나왔는지 세는 수
div = 1 # 1부터 차례대로 나누는 수
while True:
    if cnt == y:
        div -= 1
        break
    elif x + 1 == div:
        break
    if x % div == 0:
        div += 1
        cnt += 1
    else:
        div += 1
if cnt < y:
    print(0)
else:
    print(div)
# 처음에
# elif x == div:
#   break
# 로 했다가 틀렸는데
# 그 이유는 x 자체도 x의 약수이기 때문이다.

# 다른 사람이 푼 방법
# 나도 리스트에 넣을까 고민했는데
# 오래 걸릴 줄 알았는데 오히려 시간이 더 짧게 나왔다.
# N, k = map(int,input().split())
# list_0 = []
# for i in range(1,N+1):
#   if N % i == 0:
#     list_0.append(i)
# if k <= len(list_0):
#   print(list_0[k-1])
# else:
#   print(0)