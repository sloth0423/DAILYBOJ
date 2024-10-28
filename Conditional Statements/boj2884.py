X = input()
x, y = X.split()
x = int(x)
y = int(y)
if(y>= 45):
    print(x,y-45)
elif(y<45 and x != 0):
    print(x-1,60+(y-45))
elif(y<45 and x == 0):
    print(24-1, 60+(y-45))