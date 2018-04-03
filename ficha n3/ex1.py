numero=int(input("Introduza o numero de asteriscos: "))

print("Os 5 números anteriores a {} são: ".format(numero))
for i in range(numero-1, numero-6, -1):
    print(i, end=" ")