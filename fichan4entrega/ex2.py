
euro = 1.231
dolar = 0.8089
 
def conversaoeuro (quantidade):
    return (quantidade * 1.231) / 1

def conversaodolar (quantidade):
    return (quantidade *  0.8089) /  1

def teste(): 
    escolha = input("Escolha a conversao que quer utilizar E ou D:") 
    quantidade =float(input ("Introduza a quantidade que quer converter em euros e dolares: "))
    if escolha == "E" :
        print ("{}€ sao {}$".format(quantidade,conversaoeuro(quantidade)))       
    elif escolha == "D" :
        print ("{}$ sao {}€ ".format(quantidade,conversaodolar(quantidade)))         


teste()