from decimal import Decimal

i = 0
j = 1
while(i <= 2):
    print('I={} J={}'.format(i, j))
    j = j + 1
    if(j == (i + 4)):
        i += Decimal('0.2')
        j -= Decimal('2.8')