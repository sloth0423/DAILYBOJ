def hanoi(org, num, dest):
    if num == 1:
        print(f"{org} {dest}")
        return
    tmp = 6 - org - dest
    hanoi(org, num-1, tmp)
    print(f"{org} {dest}")
    hanoi(tmp, num-1, dest)

N = int(input())
print(2**N-1)
hanoi(1, N, 3)

# 처음에 푼 방법
# 그런데 생각해보니까 어차피 순서대로 return이 되기 때문에
# 굳이 list에 담아놓을 필요가 없었다.
# def hanoi(org, num, dest):
#     if num == 1:
#         return [f"{org} {dest}"]
#     tmp = 6 - org - dest
#     return hanoi(org, num-1, tmp) + [f"{org} {dest}"] + hanoi(tmp, num-1, dest)
#
# N = int(input())
# print(2**N-1)
# ls = list(hanoi(1, N, 3))
# print("\n".join(ls))

