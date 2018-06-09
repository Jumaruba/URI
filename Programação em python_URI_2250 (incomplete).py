linhas = int(input())

while linhas != 0:
    dicionario = {}
    for i in range(linhas):
        x = list(input().split())
        nome = x.pop(0)
        x = [int(a) for a in x]
        x.remove(max(x))
        x.remove(min(x))
        soma = sum(x)
        dicionario[soma] = nome
    for j in range(linhas):
        dicionario.values()

