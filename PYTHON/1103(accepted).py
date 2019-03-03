h1, m1, h2, m2 = map(int,input().split())

while h1!=0 or m1!= 0 or h2!= 0 or m2!=0:
    if h2==0:
        h2=24
    if h1==0:
        h1=24
    if m2>=m1:
        minutos=m2-m1
    else:
        minutos=m2+60-m1
        h2-=1
    if h2>=h1:
        horas = h2-h1
    else:
        horas = 24-h1+h2
    minutos = minutos +horas*60
    if h1==h2==m1==m2:
        minutos = 1440
    print(minutos)
    h1, m1, h2, m2 = map(int, input().split())

#PROBLEMA DO CASO 3 3 3 3, REPOSTA 1440
