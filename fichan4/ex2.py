def soma(numero1,numero2):
    return numero1 + numero2

def subtraçao(numero1,numero2):
    return numero1 - numero2

def divisao(numero1,numero2):
    return numero1 / numero2

def multiplicacao(numero1,numero2):
    return numero1 * numero2  


numero1 = int(input("Introduza o primeiro numero: "))

numero2 = int(input("Introduza o segundo numero: "))

operaçao=input("Introduza a operacao (+),(-),(*) e (/): ")

if operaçao == "+":
    resultado = soma(numero1,numero2)
    print("{} = {} + {}".format(resultado,numero2,numero1))
elif operaçao == "-":
    resultado = subtraçao(numero1,numero2)
    print("{} = {} - {}".format(resultado,numero2,numero1)) 
elif operaçao == "/":
    resultado = divisao(numero1,numero2)
    print("{} = {} - {}".format(resultado,numero2,numero1))    
elif  operaçao == "*":
    resultado = multiplicacao(numero1,numero2,)
    print("{} = {} - {}".format(resultado,numero2,numero1))              