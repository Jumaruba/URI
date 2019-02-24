x = int(input())
lista = []
elementos = []
for i in range(0, x):
    k = int(input())
    lista.append(k)
    lista.sort()
for i in range(0, len(lista)):
    vezes = lista.count(lista[i])
    if lista[0:i+1].count(lista[i])==1:
        print('%i aparece %i vez(es)' % (lista[i], vezes))

#tempo excedido
