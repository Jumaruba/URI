hora_inicio, min_inicio, hora_fim, min_fim = map(int, input().split())

while hora_inicio !=0 or  min_inicio != 0 or hora_fim != 0 or min_fim != 0:
    if hora_inicio == hora_fim == min_fim == min_inicio:
        print('1440')
    else:
        if min_fim >= min_inicio:
            min = min_fim - min_inicio
        else:
            hora_fim -= 1
            min = min_fim + 60 - min_inicio
        if hora_fim >= hora_inicio:
            hora = hora_fim - hora_inicio
        else:
            hora = 24 - hora_inicio + hora_fim


        min += hora * 60
        print(min)
    hora_inicio, min_inicio, hora_fim, min_fim = map(int, input().split())
