a, g, ra, rg = map(float, input().split())

al = ra / a
ga = rg / g

if al > ga:
    print('A')
else:
    print('G')
