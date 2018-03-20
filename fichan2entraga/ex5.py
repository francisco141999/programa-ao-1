saldo = input ("O seu saldo da sua conta bancaria: ")
debitar = input ("O saldo a debitar: ")



if saldo > debitar:
    print("o debito foi realizado com sucesso.")
elif saldo < debitar:
    print("Operaçao impossivel por saldo insuficiente.")

dinheiro = saldo - debitar
print("Ainda tem {}".format(dinheiro))



