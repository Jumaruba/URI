cidade = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte", 0]
DDD = [61, 71, 11, 21, 32, 19, 27, 31, 0]
x = int(input())
k=0

if x in DDD:
    for i in range (0,9):
     if DDD[i]==x:
        k=i
    print(cidade[k])

else:
    print("DDD nao cadastrado")