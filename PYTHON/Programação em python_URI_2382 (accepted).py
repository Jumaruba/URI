
largura , altura, profundidade, raio = map(int, input().split())

diagonal_2 = largura**2+altura**2+profundidade**2
#raio*2>=diagonal

if diagonal_2<=raio**2*4:
    print('S')
else:
    print('N')
