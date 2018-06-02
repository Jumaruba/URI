x = list(map(int, input().split()))

while x[0] != 0:
    vel_2, dias, vel_1 = x[0], x[1], x[2]
    n = (dias * vel_1 * vel_2) // (vel_1 - vel_2)
    if n != 1:
        print(n, 'paginas')
    else:
        print(n, 'pagina')
    x = list(map(int, input().split()))
