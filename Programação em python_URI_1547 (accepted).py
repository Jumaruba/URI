x= int(input())

def ganhador():
    quantidade, numero = map(int,input().split())
    lista = list(map(int,input().split()))
    diferenca = abs(numero-lista[0])
    sorteado_index=0
    for i in range (1,quantidade):
        if abs(numero-lista[i])<diferenca:
            diferenca = abs(numero-lista[i])
            sorteado_index = i
    print(sorteado_index+1)

for i in range (0,x):
    ganhador()
