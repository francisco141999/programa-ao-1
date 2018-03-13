valor1 = float(input("Introduza o valor: "))
valor2 = float(input("Introduza o valor: "))
valor3 = float(input("Introduza o valor: "))

calculo1 = (valor1 * 25)
calculo2 = (valor2 * 35)
calculo3 = (valor3 * 40)

calculo = calculo1 + calculo2 + calculo3
media = calculo/100
inteiro = calculo//100
modulo = calculo % 100

print("A media das 3 notas é {0:.2f} ".format(media))
print("A divisao inteira é {} e modulo da divisao é {} ".format(int(inteiro),int(modulo)))