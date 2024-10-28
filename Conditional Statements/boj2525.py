X = input()
x, y = X.split()
Z = input()
x = int(x)
y = int(y)
z = int(Z)
if ((y+(z%60)) < 60):
    print(((x+(z//60))%24),((y+(z%60))%60))
elif((y+(z%60)) >= 60):
    print((((x + (z // 60))+1) % 24) , ((y + (z % 60)) % 60))