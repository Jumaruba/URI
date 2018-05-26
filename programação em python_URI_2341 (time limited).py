quantidade, diferentes = map(int, input().split())

x = list(map(int, input().split()))
lista = []
for i in range(1, diferentes + 1):
    valor = x.count(i)
    lista.append(valor)

print(min(lista))