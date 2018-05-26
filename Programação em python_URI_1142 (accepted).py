x = int(input())

def linha(i):
    for j in range (1,(i*4+1)):
        if j%4!=0:
            print(j, end=" ")
        else:
            print('PUM')

linha(x)