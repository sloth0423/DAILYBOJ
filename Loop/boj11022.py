import sys

input = lambda: sys.stdin.readline().rstrip()

testCase = input()
testCase = int(testCase)

for i in range(1,testCase+1):
    inputNum = input()
    testNum1, testNum2 = inputNum.split()
    testNum1 = int(testNum1)
    testNum2 = int(testNum2)
    print(f"Case #{i}: {testNum1} + {testNum2} =",testNum1+testNum2)