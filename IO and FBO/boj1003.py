testCase = int(input())

findOne = 0
findZero = 0
def fibonacci(num):
    global findZero
    global findOne
    if num == 0:
        findZero += 1
        return 0
    elif num == 1:
        findOne += 1
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(testCase):
    findOne = 0
    findZero = 0
    X = int(input())
    fibonacci(int(X))
    print(str(findZero) + " " + str(findOne))







