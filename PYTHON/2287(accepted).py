x = int(input())


def digitos():  # armazenando a senha analisando o vetor senha
    global senha, x
    numeros = []  # armazena a senha de fato
    for i in range(0, 6):
        maior = 0
        quero = 0
        for j in range(0, x * 2):
            maior_novo = senha[i].count(senha[i][j])
            if maior_novo > maior:
                quero = senha[i][j]
                maior = maior_novo
        numeros.append(quero)
    return numeros


contador = 1
letras = ['A', 'B', 'C', 'D', 'E']
while x != 0:
    senha = [[-1], [-1], [-1], [-1], [-1], [-1]]
    for i in range(0, x):
        frase = str(input())
        frase = frase.replace(' ', '')
        for j in range(10, 16):
            if frase[j] == 'A':
                senha[j - 10].append(frase[0])
                senha[j - 10].append(frase[1])
            elif frase[j] == 'B':
                senha[j - 10].append(frase[2])
                senha[j - 10].append(frase[3])
            elif frase[j] == 'C':
                senha[j - 10].append(frase[4])
                senha[j - 10].append(frase[5])
            elif frase[j] == 'D':
                senha[j - 10].append(frase[6])
                senha[j - 10].append(frase[7])
            elif frase[j] == 'E':
                senha[j - 10].append(frase[8])
                senha[j - 10].append(frase[9])

    numeros = digitos()
    print('Teste', contador)
    for g in range(0, 6):
        print(numeros[g], end=' ')
    print('')
    print('')
    x = int(input())
    contador += 1

