nota1 = float(input("Introduza o valor da primeira nota (0-20): "))
nota2 = float(input("Introduza o valor da segunda nota (0-20): "))
nota3 = float(input("Introduza o valor da terceira nota (0-20): "))


if (nota1 < 0 and nota1 > 20) or (nota2 < 0 and nota2 > 20) or (nota3 < 0 and nota3 > 20); 
    nota1 = float(input("Introduza o valor da primeira nota (0-20): "))
    nota2 = float(input("Introduza o valor da segunda nota (0-20): "))
    nota3 = float(input("Introduza o valor da terceira nota (0-20): "))
else:
    media = float((nota1 * 25 + nota2 * 35 + nota3 * 40) / 100)

if media >= 9,5:
    print("aprovado")
else:
    print("reprovado")
        
   

