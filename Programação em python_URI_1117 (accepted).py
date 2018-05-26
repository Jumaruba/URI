k=2
media=0
numinvalidos=0
while k!=0:
    x = float(input())
    if x>=0 and x<=10:
        media+=x
        k-=1
    else:
        numinvalidos+=1

media= media/2
media= '%.2f' %media

for i in range(0,numinvalidos):
    print('nota invalida')

print('media =', media)

