quantidade = int(input())

x = len(set([input() for i in range(quantidade)]))

print('Falta(m) {} pomekon(s).'.format(151 - x))


