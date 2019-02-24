x = eval(input())

if 0<=x<=400:
    reaj= 0.15 * x
    novo= x+reaj
    print("Novo salario: %.2f" %novo)
    print("Reajuste ganho: %.2f" %reaj)
    print("Em percentual: 15 %")
elif 400.01<=x<=800.00:
    reaj = 0.12 * x
    novo = x + reaj
    print("Novo salario: %.2f" % novo)
    print("Reajuste ganho: %.2f" % reaj)
    print("Em percentual: 12 %")
elif 800.01<=x<=1200:
    reaj = 0.10 * x
    novo = x + reaj
    print("Novo salario: %.2f" % novo)
    print("Reajuste ganho: %.2f" % reaj)
    print("Em percentual: 10 %")
elif 1200.01<=x<=2000:
    reaj = 0.07 * x
    novo = x + reaj
    print("Novo salario: %.2f" % novo)
    print("Reajuste ganho: %.2f" % reaj)
    print("Em percentual: 7 %")
elif x>2000:
    reaj = 0.04 * x
    novo = x + reaj
    print("Novo salario: %.2f" % novo)
    print("Reajuste ganho: %.2f" % reaj)
    print("Em percentual: 4 %")
