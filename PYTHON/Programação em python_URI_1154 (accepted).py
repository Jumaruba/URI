n = int(input())
quantidade = 0
soma = 0
while n >= 0:
    quantidade += 1
    soma+=n
    n = int(input())


k = soma/quantidade
print('%.2f' %k)

