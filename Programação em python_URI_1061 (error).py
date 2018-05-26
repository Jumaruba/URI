l = input()
j = l.split()
m = str(j[0])
dia1 = int(j[1])
h1,  m1, s1 = map(int, input().split(" : "))
l2 = input()
j2 = l2.split()
m2 = str(j2[0])
dia2 = int(j[1])
h2,  m2, s2 = map(int, input().split(" : "))
segundos =0
minutos =0
horas=0
dias=0
aux=0
aux2=0

if dia1!=dia2:
    dias=dia2-dia1-1
    segundos = 60 - s1 +s2
    if segundos>=60:
        segundos-=60
        minutos= 60-m1+m2+aux
    else:
        minutos= 59-m1+m2

    if minutos>=60:
        minutos-=60
        horas= 24-h1+h2
    else:
        horas= 23-h1+h2

    if horas>=24:
        aux2=horas//24
        horas=horas%24
        dias+=aux2

    print('%i dia(s)'%dias)
    print('%i hora(s)'%horas)
    print('%i minuto(s)'%minutos)
    print('%i segundo(s)' %segundos)

elif dia1==dia2:
    if s2>s1:
        segundos=s2-s1
    else:
        segundos=60+s2-s1
        m2-=1
    if m2>m1:
        minutos=m2-m1
    else:
        minutos=60+m2-m1
        horas-=1
    horas= h2-h1
    print('%i dia(s)'%dias)
    print('%i hora(s)'%horas)
    print('%i minuto(s)'%minutos)
    print('%i segundo(s)' %segundos)

