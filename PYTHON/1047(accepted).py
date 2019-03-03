i, im, f, fm = map(int, input().split())

if f>i and fm>=im:
    h = f-i
    m = fm-im
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif f>i and im>fm:
    h = f-1-i
    m = fm+60-im
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i>f and fm>=im:
    h= 24-i+f
    m = fm-im
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i>f and im>fm:
    h = 24 - i + f -1
    m = fm+60-im
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif f==i and fm>im:
    h = 0
    m = fm - im
    print("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" %(h,m))
elif i==f and im==fm:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")