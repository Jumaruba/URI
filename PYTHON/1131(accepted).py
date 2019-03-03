vitorias_inter=0
vitorias_gremio=0
empates = 0
grenais = 0
choice =1

while choice==1:
    inter, gremio = map(int, input().split())

    if inter>gremio:
        vitorias_inter+=1
    elif gremio>inter:
        vitorias_gremio+=1
    else:
        empates+=1
    grenais+=1
    choice = int(input('Novo grenal (1-sim 2-nao)\n'))


print('%i grenais' %grenais)
print('Inter:%i' %vitorias_inter)
print('Gremio:%i' %vitorias_gremio)
print('Empates:%i' %empates)
if vitorias_inter>vitorias_gremio:
    print('Inter venceu mais')
elif vitorias_gremio>vitorias_inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')