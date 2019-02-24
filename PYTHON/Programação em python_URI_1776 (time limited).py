def divisor(numero):  # CORRETO (APENAS NUMEROS PRIMOS)
    numeros = []
    produto = 1
    for i in range(2, numero // 2 + 1):
        if numero % i == 0 and len(divisor(i)) == 0:
            numeros.append(i)
            produto *= i
    return numeros


def quadrado_perfeito(numero):  # CORRETO
    raiz = int(numero ** 0.5)
    if raiz ** 2 != numero:
        return False
    else:
        return True


def multiplicar(divisores, numero):
    multiplica = 1
    contador = 0
    for i in range(len(divisores)):
        while numero % divisores[i] == 0: #QUANTAS VEZES O DIVISOR PRIMO SE REPETE
            contador += 1
            numero = numero / divisores[i]
        if contador % 2 != 0:
            multiplica *= divisores[i]
        contador = 0
    return multiplica


testes = int(input())

for i in range(testes):
    numero = int(input())
    boleana = quadrado_perfeito(numero)
    if boleana:  # CASO SEJA QUADRADO PERFEITO
        resultado = numero
    else:  # SE NÃO FOR QUADRADO PERFEITO
        divisores = divisor(numero)  # ACHAMOS OS DIVISORES
        if len(divisores) == 0:  # SE O NUMERO FOR PRIMO
            resultado = numero ** 2
        else:
            multiplica = multiplicar(divisores, numero)
            resultado = numero * multiplica

    print('Caso #%i: %i' %(i+1,resultado))

#EXCEDEU TEMPO LIMITE
