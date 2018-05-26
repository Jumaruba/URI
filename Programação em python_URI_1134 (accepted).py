def ler ():
    x= int(input())
    if 1<=x<=4:
        return x
    else:
        return ler()

alcool=0
gasolina=0
diesel=0
x=9
while x!=4:
    x = ler()
    if x ==1:
        alcool+=1
    elif x==2:
        gasolina+=1
    elif x==3:
        diesel+=1

print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gasolina)
print('Diesel:', diesel)
