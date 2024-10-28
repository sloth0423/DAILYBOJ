X = input()
x,y,z = X.split()
x = int(x)
y = int(y)
z = int(z)
if( x == y and y == z):
    print(10000+(x)*1000)
elif( x == y and y != z):
    print(1000+x*100)
elif( x == z and z != y):
    print(1000+x*100)
elif( y == z and z != x):
    print(1000+y*100)
elif( x != y and y != z):
    print(max(x,y,z)*100)