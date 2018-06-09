quantidade, diferentes = map(int, input().split())

lista = list(map(int, input().split()))
menor = lista.count(1)
for i in range(2, diferentes + 1):
    numero = lista.count(i)
    if numero < menor:
        menor = numero

print(menor)
