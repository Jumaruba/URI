def numeros(x):
    for i in range (1,x):
        print(i, end=' ')
    print(x)

x= int(input())
while x!=0:
    numeros(x)
    x = int(input())