x = input()


def substitui(resultado):
    resultado = resultado.replace('7', '0')
    return resultado


if '+' in x:
    primeiro, separador, segundo = x.partition(' + ')
    resultado = substitui(str(int(substitui(primeiro)) + int(substitui(segundo))))

else:
    primeiro, separador, segundo = x.partition(' x ')
    resultado = substitui(str(int(substitui(primeiro)) * int(substitui(segundo))))

print(int(resultado))
