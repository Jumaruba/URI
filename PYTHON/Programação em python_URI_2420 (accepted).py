x = int(input())
lista = list(map(int, input().split()))
tamanho = sum(lista) / 2
soma = 0
for i in range(x):
    soma += lista[i]
    if soma == tamanho:
        print(i + 1)
        break
