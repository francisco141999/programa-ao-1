def conteudo_lista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")

def dobro(lista):
    for i in range(len(lista)):
        print(lista[i]*2,end=" ")

def soma(lista):
    contar = 0
    for numero in lista:
        contar += numero
    return contar 

def media(lista):
    contar = 0
    for numero in lista:
        contar += numero
    return contar /len(lista)

numero = []
x = 1
while x <= 10:
    y = int(input('Intoduza um número: [ %s ]: '%x))
    numero.append(y)
    x += 1


print('\nConteúdo da lista:') 
conteudo_lista(numero)
print('\nDobro de cada elemento:') 
dobro(numero)
print('\n\nSoma da lista:', soma(numero))
print('\nMedia da lista:', media(numero))
print("\nMaior número da lista é:", max(numero))
print("\nMenor número da lista é:", min(numero))