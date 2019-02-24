x = int(input())
c = 0
r = 0
s = 0
soma = 0
for i in range (0,x):
    l = input()
    q, tipo = l.split()
    q = int(q)
    tipo = str(tipo)
    if tipo == 'C':
        c+=q
    elif tipo == 'R':
        r+=q
    elif tipo == 'S':
        s+=q
    soma+=q
pc = (100*c)/soma
pr = (100*r)/soma
ps = (100*s)/soma


print('Total: %i cobaias' %soma)
print('Total de coelhos: %i' %c)
print('Total de ratos: %i' %r)
print('Total de sapos: %i' %s)
print('Percentual de coelhos: %.2f %%' %pc)
print('Percentual de ratos: %.2f %%' %pr)
print('Percentual de sapos: %.2f %%' %ps)
