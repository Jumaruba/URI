m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
vet_aux = []


def n_list(l):
    x, y = map(int, input().split())
    if x > y:
        vet_aux.append(2 * l + 1)
    else:
        vet_aux.append(2 * l)
    return vet_aux


def n_list_2(vet_aux):
    for p in (len(vet_aux), -1, -1):
        print(vet_aux)
        m.pop(vet_aux[p])
    return m


for i in range(8):
    auxiliar = n_list(i)
m = n_list_2(vet_aux)
auxiliar = []

for j in range(4):
    auxiliar = n_list(j)
m = n_list_2(vet_aux)
auxiliar = []

for k in range(2):
    vet_aux = n_list(k)
m = n_list_2(vet_aux)
auxiliar = []

print(print(min(m)))
