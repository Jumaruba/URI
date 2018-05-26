def matriz ():
    global tamanho
    matriz=[]
    for i in range(0,tamanho):
            x = list(map(int,input().split()))
            matriz.append(x)
    return matriz

tamanho = int(input())
matriz = matriz()
borb_coletadas = []
for i in range(0,tamanho*2):
    linha, coluna = map(int,input().split())
    borboleta = matriz[linha-1][coluna-1]
    if borboleta not in borb_coletadas:
        borb_coletadas.append(borboleta)

print(len(borb_coletadas))