def numero (linha, coluna, carater) :
     
    for i in range(1, linha + 1) :
        for e in range(1, coluna + 1) :
            if (i == 1 or i == linha or e == 1 or e == coluna) :
                print(carater, end="")            
            else :
                print(" ", end="")            
        print()
 
 
carater = int(input("Introduza o numero do carater que quer utilizar: "))
linha = int(input("Introduza o numero da linha que quer utilizar: "))
coluna = int(input ("Introduza o numero da coluna que quer utilizar : "))

numero(linha, coluna, carater)