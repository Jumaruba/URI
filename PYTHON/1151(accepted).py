x = int(input())

a = 0
b = 1
print(0, end=' ')
print(1, end=' ')
contador = 2

while contador != x - 1:
    c = a + b
    a = b
    b = c
    contador += 1
    print(c, end=' ')
print(a + b)
