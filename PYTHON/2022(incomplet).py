def por_querer(dicionario):
    
def menor_preco(dicioanario):

def ordem_alfabetica(dicionario):


dicionario = {}
while True:
    try:
         nome, entradas = input().split()
         entradas = int(entradas)
         for i in range(entradas):
             presente = str(input())
             preco, querer = map(eval, input().split())
             dicionario[presente] = [preco, querer]

        print('Lista de', nome)


    except:
        break