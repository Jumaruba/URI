def checagem(real, falso):
    global falsas
    total = 0
    for i in range(len(real)):
        if real[i] != falso[i]:
            total += 1
    if total > 1:
        return True
    else:
        return False


quantidade = int(input())

while quantidade != 0:
    falsas = 0
    dicionario = {}

    for i in range(quantidade):
        nome, assinatura = map(str, input().split())
        dicionario[nome] = assinatura

    apareceram = int(input())

    for j in range(apareceram):
        nome, assinatura = map(str, input().split())
        boleana = checagem(dicionario[nome], assinatura)
        if boleana:
            falsas+=1

    print(falsas)
    quantidade = int(input())
