x= int(input())
def valores ():
    global x
    y = int(input())
    if y<=x:
        return valores()
    else:
        return y


contador = 1
maior= valores()
soma= x
while maior>soma:
    x+=1
    soma+=x
    contador+=1

print(contador)
