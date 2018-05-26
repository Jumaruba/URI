soma=0
x = int(input())
y = int(input())

if x>y:
    maior=x
    menor=y
elif x<y:
    maior=y
    menor=x

if x!=y:
    for i in range (menor, maior+1):
        if i%13!=0:
            soma+=i
    print(soma)
elif x==y:
    if x%13!=0:
        print(x)
    else:
        print(0)
