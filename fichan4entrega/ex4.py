def numero(numero_max):
    if numero_max == -1:
        return 0
    elif numero(numero_max - 1):
        return numero_max
    print(numero_max)

num = int(input('Introduza um numero maximo: '))

numero(num)