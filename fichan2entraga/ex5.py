saldo = float(input ("O seu saldo da sua conta bancaria: "))
print("Operaçao que quer realizar: ")
print ('1-deposito')
print ('2-debito')
operacao = input("Introduzaa operaçao que quer realizar: ")

if operacao == '1' :
    deposito = float(input ("O Deposito na sua conta: "))
    valor = saldo + deposito
    print('Ficou com um saldo de: ', valor)
elif operacao == '2' : 
    debito = float(input ("O dinheiro a debitar: "))
    valor = saldo - debito
    if valor < 0 :
        print('Operaçao impossivel por saldo insuficiente')
    else :
        print('Ficou com um saldo de: ', valor)


