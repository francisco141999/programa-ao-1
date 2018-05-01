def adicionar(lista):
    for i in range(0,10):
        caracter = input("Introduzza um caracter: ")
        lista.append(caracter)
    print("Lista: ",lista)

def posição(lista):
    vercart = input("Carater: ")
    contar = lista.count(vercart)
    print("O {} existe: {} vezes.".format(vercart,contar)) 
    for i,j in enumerate(lista):
        if j == vercart:
            print("O {} encontra-se na posição {} .".format(j,i))

lista = []

adicionar(lista)

posição(lista)