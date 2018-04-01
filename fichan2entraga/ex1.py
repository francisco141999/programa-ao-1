pnota1= .25
pnota2= .35
pnota3= .40

#Nota1
nota1 = float(input("Introduza a primeira nota: "))
while nota1 < 0.0 or nota1 > 20.0:
    nota1 = float(input("Introduza a primeira nota: "))

#Nota2
nota2 = float(input("Introduza a segunda nota: "))
while nota2 < 0.0 or nota2 > 20.0:
    nota2 = float(input("Introduza a segunda nota: "))

#Nota3
nota3 = float(input("Introduza a terceira nota: "))
while nota3 < 0.0 or nota3 > 20.0:
    nota3 = float(input("Introduza a terceira nota: "))

#Média
media = int((nota1 * pnota1 + nota2 * pnota2 + nota3 * pnota3))

if media >= 9.5 :
    print("Aprovado com {} (valor arredondado)".format(media))
else :
    print("Reprovado com {} (valor arredondado)".format(media))