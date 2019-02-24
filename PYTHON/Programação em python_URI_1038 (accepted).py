
cod, qty = input (). split ()
cod = int (cod)
qty = int (qty)
if (cod == 1):
    total = qty * 4
elif (cod == 2):
    total = qty * 4.5
elif (cod == 3):
    total = qty * 5
elif (cod == 4):
    total = qty * 2
elif (cod == 5):
    total = qty * 1.5
print ( "Total: R $% .2f" % total)