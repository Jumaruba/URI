area, lado1, lado2 = map(int, input().split())
while area != 0 or lado1 != 0 or lado2 != 0:
    c1, c2, c3 = map(int, input().split())
    lado1 = lado1 + 1
    lado2 = lado2 + 1
    s_maior = round(((c3 * c1 * area)/(lado1*lado2)),3)
    s_menor = round(((c1 * c2 * area)/(lado1*lado2)),3)
    print(int(abs(s_maior - s_menor)))
    area, lado1, lado2 = map(int, input().split())
