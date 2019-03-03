quantidade = int(input())

for i in range(quantidade):
    diamante = input()
    diamante.count('.')
    map(lambda diamante: diamante.remove('.'), diamante)