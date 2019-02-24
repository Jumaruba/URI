print('HALL OF MURDERERS')
dicionario = {}
for i in range(3):

    assassino = str(input())
    morto = str(input())
    dicionario[assassino] = []
    dicionario[assassino].append(morto)
    if morto in dicionario:
        dicionario[morto] = 0

for i in dicionario:
    if dicionario[i] != 0:
        print(dicionario[i], len(dicionario[i]))
