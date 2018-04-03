numero=int(input("Introduza um número "))
if numero == 2:
    print("O número {} é primo".format(numero))
else:
    while numero > 1:
        for i in range(2,numero):
            if numero % i == 0:
                print("O número {} não é primo".format(numero))
                break
            else:
                print("O número {} é primo".format(numero))
                break
        break
if numero <= 1:
    print("Para ser primo tem de ser superior a 1, por isso o número {} não é possivel",format(numero))