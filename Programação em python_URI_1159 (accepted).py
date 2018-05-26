def soma_pares ():
    global x
    soma=0
    if x%2==0:
        primeiro=x
        ultimo = x+10
    if x%2==1:
        primeiro=x+1
        ultimo= x+11
    for i in range (primeiro,ultimo,2 ):
        soma+=i
    print(soma)

x = int(input())
while x!=0:
    soma_pares()
    x= int(input())