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
else:
# elif( x != y and y != z and x != z): # 혼자 생쇼함 ㅋㅋ;
    if(x>y and x>z):
        print(x*100)
    if(y>x and y>z):
        print(y*100)
    if(z>x and z>y):
        print(z*100)
    #print(max(x,y,z)*100) // max() 함수를 안다고 생각했을 때 풀이