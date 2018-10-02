x = int(input())

n = []
frase = input()
alpha = 'abcdefghijklmnoprstuvwxyz'

for i in range(x):
    for i in range (len(frase)):
        if i in alpha and i not in n:
            n.append(lower(i))
        if len(n) == len(alpha)//2:
            print('frase quase completa')
        elif len(n)= len(alpha):
            print('frase completa')
        else:
            print('frase mal elaborada')
