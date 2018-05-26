def trocando(algarismo):
    novo = algarismo[-1]
    for i in range(len(algarismo) - 2, -1, -1):
        primeiro = algarismo[i]
        novo += primeiro
    return novo


def algorismos(palavra):
    primeiro, separador, resultado = palavra.partition('=')
    resultado = int(trocando(resultado))
    soma_1, sinal, soma_2 = primeiro.partition('+')
    soma_1 = int(trocando(soma_1))
    soma_2 = int(trocando(soma_2))

    if soma_1 + soma_2 == resultado:
        print(True)
    else:
        print(False)


palavra = input()
while palavra != '0+0=0':
    algorismos(palavra)
    palavra = input()
print(True)