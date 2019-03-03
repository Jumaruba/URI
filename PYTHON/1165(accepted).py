n = int(input())

def numero_primo ():
    global x
    k = True
    for i in range (2,x//2+1):
        if x%i==0:
            k = False
    return k

for i in range (0,n):
    x = int(input())
    k = numero_primo()
    if k == True:
        print(x, 'eh primo')
    else:
        print(x,'nao eh primo')