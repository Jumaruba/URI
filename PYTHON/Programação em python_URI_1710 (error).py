def prod_escalar(plano, ponto):
    return plano[0] * ponto[0] + plano[1] * ponto[1] + plano[2] * ponto[2]


planos, planetas = map(int, input().split())

planetas_coord = []
planos_eq = []

for j in range(planos):
    x = list(map(int, input().split()))
    planos_eq.append(x)
for i in range(planetas):
    x = list(map(int, input().split()))
    planetas_coord.append(x)

regioes = [0 for k in range(planos + 1)]

for m in planetas_coord:
    regiao = False
    for n in range(len(planos_eq)):
        if prod_escalar(planos_eq[n], m) < planos_eq[n][3] and not regiao:
            regioes[n] += 1
            regiao = True
    if not regiao:
        regioes[len(planos_eq)] += 1

print(max(regioes))
