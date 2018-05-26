conhece, tamanho = map(int, input().split())
nome_list = []
contador = 0
while contador!= conhece:
    nome = str(input())
    unidades = int(nome[-1])
    if nome[-2] != ' ':
        dezenas = int(nome[-2])
        if nome[-3] != ' ':
            centenas = int(nome[-3])
            if nome[-4]!= ' ':
                milhares = int(nome[-4])*1000
                nome = nome[0:len(nome) - 4]
                altura = milhares +centenas*100 + dezenas*10 + unidades
            else:
                nome = nome[0:len(nome) - 3]
                altura = centenas*100 + dezenas*10 + unidades
        else:
            nome = nome[0:len(nome) - 2]
            altura = dezenas * 10 + unidades
    else:
        nome = nome[0:len(nome) - 1]
        altura = unidades

    if altura > tamanho:
        print(nome)
    contador+=1


