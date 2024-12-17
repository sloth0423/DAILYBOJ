import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
n = int(input())  # 명령의 수
dq = deque()  # 덱 선언

for _ in range(n):
    command = input().split()  # 명령어 입력받기
    if command[0] == '1':  # 1 X: 정수 X를 덱의 앞에 넣는다
        dq.appendleft(int(command[1]))
    elif command[0] == '2':  # 2 X: 정수 X를 덱의 뒤에 넣는다
        dq.append(int(command[1]))
    elif command[0] == '3':  # 3: 덱의 가장 앞에 있는 수를 빼고 출력
        print(dq.popleft() if dq else -1)
    elif command[0] == '4':  # 4: 덱의 가장 뒤에 있는 수를 빼고 출력
        print(dq.pop() if dq else -1)
    elif command[0] == '5':  # 5: 덱에 들어있는 정수의 개수 출력
        print(len(dq))
    elif command[0] == '6':  # 6: 덱이 비어있으면 1, 아니면 0
        print(1 if not dq else 0)
    elif command[0] == '7':  # 7: 덱의 가장 앞에 있는 정수 출력
        print(dq[0] if dq else -1)
    elif command[0] == '8':  # 8: 덱의 가장 뒤에 있는 정수 출력
        print(dq[-1] if dq else -1)