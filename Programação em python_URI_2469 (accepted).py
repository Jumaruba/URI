x = int(input())
lista = list(map(int, input().split()))
l = set(lista)
maior = 0
for i in l:
    agora = lista.count(i)
    if agora > maior:
        numero = i
        maior = agora
    elif agora == maior:
        if i>numero:
            numero = i

print(numero)
