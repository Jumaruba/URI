def resto(menor, maior):
    for i in range (menor+1,maior):
        if i%5==2 or i%5==3:
            print(i)

x = int(input())
y = int(input())

if x>y:
    maior=x
    menor=y
elif x<y:
    maior=y
    menor=x
else:
    maior=x
    menor=x

resto(menor,maior)
