AA, BB = map(int, input().split())
A = AA
B = BB
while A % B != 0:
    R = A % B
    A = B
    B = R
print(AA*BB//B)