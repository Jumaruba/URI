def cpf_d1():
    global x, d1
    soma = 0
    for i in range (0,9):
        k = int(x[i])*(i+1)
        soma +=k
    if (soma%11)%10==d1:
        return True
    else:
        return False


def cpf_d2():
    global x, d2
    soma = 0
    for i in range(0, 9):
        k = int(x[i]) * (9-i)
        soma += k
    if (soma%11)%10==d2:
        return True
    else:
        return False

while True:
  try:
    x = list(input())
    x.pop(3)
    x.pop(6)
    d1 = int(x[10])
    d2 = int(x[11])
    for i in range(0, 3):
        x.pop(9)
    d1 = cpf_d1()
    d2 = cpf_d2()
    if d1==True and d2==True:
        print('CPF valido')
    else:
        print('CPF invalido')
  except EOFError:
      break
