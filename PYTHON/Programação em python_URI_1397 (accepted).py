quantidade = int(input())
primeiro = 0
segundo = 0
while quantidade!=0:
    for i in range(quantidade):
        x, y = map(int,input().split())
        if x> y:
            primeiro+=1
        elif y>x:
            segundo+=1
    print(primeiro, segundo)
    primeiro = 0
    segundo = 0
    quantidade = int(input())