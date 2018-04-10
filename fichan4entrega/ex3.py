carater = input("Introduza o carater que quer utilizar: ")
linha = input("Introduza o numero linha que quer utilizar: ")
coluna = input ("Introduza o numero que quer utilizar coluna: ")
def numero (linhas, colunas, caracter) :
     
    for i in range(1, linhas + 1) :
        for e in range(1, colunas + 1) :
            if (i == 1 or i == linhas or e == 1 or e == colunas) :
                print(caracter, end="")            
            else :
                print(" ", end="")            
        print()
 
 
linhas = int(input('Quantas linhas quer ter: '))
colunas = int(input('Quantas colunas quer ter: '))
caracter = input('Escolha o caracter que pretende utilizar: ')


numero(linhas, colunas, caracter)