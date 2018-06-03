cases = int(input())

while cases != 0:
    name = []
    year = []
    day = []
    auxiliar = []
    for i in range(cases):
        x = input().split()
        name.append(x[0])
        year.append(int(x[1]))
        day.append(int(x[2]))

    x = year.count(min(year))
    if x > 1:
        for k in range(x):
            auxiliar.append(year.index(min(year)))
            year[year.index(min(year))] = -1
        menor = 32
        for j in auxiliar:
            if day[j] < menor:
                menor = day[j]
        print(name[menor])
    else:
        print(name[year.index(min(year))])
    cases = int(input())
