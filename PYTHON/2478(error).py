pessoas = int(input())
lista_presentes = []
lista_pessoas = []
for i in range(pessoas):
    x = list(map(str, input().split()))
    lista_pessoas.append(x[0])
    lista_presentes.append(x[1:])

while True:
    try:
        pessoa, presente = map(str, input().split())
        index = lista_pessoas.index(pessoa)
        if presente in lista_presentes[index]:
            print('Uhul! Seu amigo secreto vai adorar o/')
        else:
            print('Tente Novamente!')
    except EOFError:
       break
