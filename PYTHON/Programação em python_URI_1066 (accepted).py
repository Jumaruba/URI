par=0
impar=0
pos=0
neg=0
for i in range (0,5):
    x = int(input())
    if x%2==0:
        par+=1
    if x%2==1:
        impar+=1
    if x>0:
        pos+=1
    elif x<0:
        neg+=1

print("%i valor(es) par(es)" %par)
print("%i valor(es) impar(es)" %impar)
print("%i valor(es) positivo(s)" %pos)
print("%i valor(es) negativo(s)" %neg)
