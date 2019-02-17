while True:
    try:

        x  = int(input())

        quantidade = len(str(x))
        superior = "1"*(quantidade+1)
        resto = int(superior)%x
        contador = quantidade + 1

        while (resto != 0):

            resto = resto * 10 +1
            resto = resto % x
            contador += 1
        print (contador)

    except EOFError:
        break

        
