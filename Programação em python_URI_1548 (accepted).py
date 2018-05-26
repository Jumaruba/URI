quantidade = int(input())

for i in range(0,quantidade):
    tamanho = int(input())
    numeros = list(map(int, input().split()))
    pessoas = numeros [:]
    pessoas.sort()
    pessoas.reverse()
    contador = 0
    for k in range(0,tamanho):
        if pessoas [k] == numeros[k]:
            contador+=1
    print(contador)