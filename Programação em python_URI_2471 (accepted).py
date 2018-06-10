x = int(input())

matrix = [list(map(int, input().split())) for i in range(x)]

def _id_():
    lista = []
    for i in range(3):
        n = sum(matrix[i])
        if n in lista:
            return n
        else:
            lista.append(n)


def linhas():
    for l in matrix:
        if sum(l) != soma:
            return matrix.index(l)


def colunas():
    for c in range(x):
        aux = []
        for l in range(x):
            aux.append(matrix[l][c])
        if sum(aux) != soma:
            return c


soma = _id_()
linha = linhas()
coluna = colunas()
numero = soma - (sum(matrix[linha]) - matrix[linha][coluna])
print(numero, matrix[linha][coluna])
