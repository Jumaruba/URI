diametro = int(input())

dados = list(map(int,input().split()))

def cabe(diamentro,dados):
    for i in dados:
        if i<diamentro:
            return False
    return True

boleana = cabe(diametro,dados)

if boleana:
    print('S')
else:
    print('N')