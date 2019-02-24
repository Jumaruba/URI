import random

pessoas = int(input())
paes = int(input())

lista = list(map(int, input().split()))
maior = sum(lista) // pessoas
soma = 0
menor = 0
x = random.randint(menor, maior)
while maior != menor+1:
    soma = 0
    for j in lista:
        soma += j // x
    if soma >= pessoas:
        menor = x
    else:
        maior = x
    x = random.randint(menor, maior)

print(menor)
