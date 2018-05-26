primeiro = int(input())
segundo = int(input())
terceiro = int(input())
minutos = []

#se o primeiro andar
total_1= segundo*2+terceiro*4
minutos.append(total_1)
#se o segundo andar
total_2 = primeiro*2+terceiro*2
minutos.append(total_2)
#se o terceiro andar
total_3 = primeiro*4+segundo*2
minutos.append(total_3)

print(min(minutos))