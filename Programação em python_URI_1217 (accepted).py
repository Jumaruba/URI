cases = int(input())
kg = 0
money = 0
for i in range(cases):
    money += float(input())
    kg_d = len(list(map(str, input().split())))
    print('day %i: %i kg' % (i+1, kg_d))
    kg += kg_d

print('%.2f kg by day' % (kg / cases))
print('R$ %.2f by day' % (money / cases))
