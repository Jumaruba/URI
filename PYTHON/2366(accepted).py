postos, intermediario = map(int, input().split())

lista = list(map(int, input().split()))
lista.append(42195)

consegue = True

for i in range(1, postos+1):
    distancia = lista[i] - lista[i - 1]
    if distancia > intermediario:
        print('N')
        consegue = False
        break
if consegue:
    print('S')
