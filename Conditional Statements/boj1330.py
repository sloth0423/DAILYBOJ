X = input()
x, y = X.split()
x = int(x)
y = int(y)
if (x > y):
    print('>')
elif (x < y):
    print('<')
else:
    print('==')
