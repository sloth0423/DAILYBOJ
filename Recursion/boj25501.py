import sys
input = lambda: sys.stdin.readline().rstrip()

def recursion(s, l, r):
    if l >= r: return 1 , l
    elif s[l] != s[r]: return 0, l
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for _ in range(T):
    S = input()
    isPal = isPalindrome(S)
    print(f"{isPal[0]} {isPal[1]+1}")

# import sys
# input = lambda: sys.stdin.readline().rstrip()
#
# def recursion(s, l, r):
#     global cnt
#     cnt += 1
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)
# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)
#
# T = int(input())
#
# for _ in range(T):
#     S = input()
#     cnt = 0
#     print(f"{isPalindrome(S)} {cnt}")
