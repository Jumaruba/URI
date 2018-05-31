x = sum(list(map(int, input().split())))

renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

resto = x % 9
print(renas[resto - 1])
