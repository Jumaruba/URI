def coluna(total_linhas,num_coluna,matriz):
    vet_coluna = []
    for linha in range(total_linhas):
        vet_coluna.append(matriz[linha][num_coluna])
    return vet_coluna
linhas, colunas = map(int, input().split())

matriz = [list(map(int, input().split())) for i in range(linhas)]

maior_soma = 0
agora_soma = 0

for j in range(linhas):
    agora_soma = sum(matriz[j])
    if agora_soma > maior_soma:
        maior_soma = agora_soma

for n in range(colunas):
    agora_soma = sum(coluna(linhas,n,matriz))
    if agora_soma>maior_soma:
        maior_soma = agora_soma

print(maior_soma)