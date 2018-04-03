def inteiro(min,max):
    numero = min-1
    while numero < min  or numero > max:
       numero = int(input("Introduza um numero: "))
    return numero  
numero  = inteiro(0,20)
   
print(numero)
