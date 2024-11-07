import sys

input = lambda: sys.stdin.readline().rstrip()

x = input()
sum = 0
for i in range(len(x)):
    if x[i] == 'A' or x[i] == 'B' or x[i] == 'C':
        sum +=3
    if x[i] == 'D' or x[i] == 'E' or x[i] == 'F':
        sum += 4
    if x[i] == 'G' or x[i] == 'H' or x[i] == 'I':
        sum += 5
    if x[i] == 'J' or x[i] == 'K' or x[i] == 'L':
        sum += 6
    if x[i] == 'M' or x[i] == 'N' or x[i] == 'O':
        sum += 7
    if x[i] == 'P' or x[i] == 'Q' or x[i] == 'R' or x[i] == 'S':
        sum += 8
    if x[i] == 'T' or x[i] == 'U' or x[i] == 'V':
        sum += 9
    if x[i] == 'W' or x[i] == 'X' or x[i] == 'Y' or x[i] == 'Z':
        sum += 10
print(sum)

