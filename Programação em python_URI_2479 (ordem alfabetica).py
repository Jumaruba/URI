quantidade = int(input())
comportados = 0
n_comportados = 0
nomes = []
for i in range(0, quantidade):
    nome = str(input())
    if nome[0] == '+':
        comportados += 1
    else:
        n_comportados += 1

    nome = nome[2:len(nome)]
    nomes.append(nome)

for j in range(0, quantidade):
    print(min(nomes))
    nomes.remove(min(nomes))

print('Se comportaram: %i | Nao se comportaram: %i' % (comportados, n_comportados))
