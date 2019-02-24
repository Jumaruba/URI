quantidade = int(input())
teste = 1
while quantidade != 0:
    diferenca = []
    boleana = False
    for i in range(0, quantidade):
        x, y = map(int, input().split())
        soma = x - y
        diferenca.append(soma)
        if x != 0 and soma > 0:
            boleana = True
    if boleana:
        soma_maior = 0
        inicio = 0
        fim = 0

        for i in range(0, len(diferenca)):
            soma = 0
            for j in range(i, len(diferenca)):
                soma += diferenca[j]

                if soma > soma_maior:
                    soma_maior = soma
                    inicio = i + 1
                    fim = j + 1
                elif soma == soma_maior and j - i > fim - inicio:
                    inicio = i + 1
                    fim = j + 1

        print('Teste', teste)
        print(inicio, fim)
    else:
        print('Teste', teste)
        print('nenhum')

    print('')
    quantidade = int(input())
    teste += 1

# tempo excedido!!
