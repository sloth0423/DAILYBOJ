N = int(input())

fiveCnt = N // 5
for i in range(fiveCnt, -1, -1):
    N2 = N - (5*i)
    if N2 % 3 == 0:
        threeCnt = N2 // 3
        print(i + threeCnt)
        break
    if i == 0 and N2 % 3 != 0:
        print(-1)
        break
# 루프문 뒤의 else절은 루프가 break문을 만나지 않고
# 정상적으로 종료되었을 때 실행된다고 함
# else:
#     print(-1)

# 다른 사람이 푼 코드
# 이 사람은 나랑 반대로 3을 먼저 빼고 5로 나누었다.
# 근데 더 빨랐다.
# 이유는 아마 bags변수에 계속 1을 출력한 뒤 바로 출력되게 해서가 아닐까?

# N = int(input())
#
# bags = 0
# while N >= 0:
#     if N % 5 == 0:
#         bags += N // 5
#         print(bags)
#         break
#     N -= 3
#     bags += 1
# else:
#     print(-1)



