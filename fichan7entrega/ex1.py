from random import randint

NUMERO_INICIAL = 0
NUMERO_FINAL=19
NUMRE_VALORES  = 5

file = open ("fichan7entrega\ex1.txt", "a")

for i in range(NUMRE_VALORES) : 
    aleatorio = str (randint(NUMERO_INICIAL,NUMERO_FINAL)) + "\n"
    print(aleatorio)
    file.write(aleatorio)

file.close()