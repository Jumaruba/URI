nome, decisao = map(str, input().split())
dicionario = {'NO': [], 'YES': []}
vencedor = 'a'

while True:
    try:
        if decisao == 'YES':
            if nome not in dicionario['YES']:
                dicionario['YES'].append(nome)
                if len(nome)>len(vencedor):
                    vencedor = nome
        else:
            dicionario['NO'].append(nome)
        nome, decisao = map(str, input().split())
    except ValueError:
        break

dicionario['YES'].sort()
dicionario['NO'].sort()

for i in (dicionario['YES']):
    print(i)
for j in (dicionario['NO']):
    print(j)

print('')
print('Amigo do Habay:')
print(vencedor)