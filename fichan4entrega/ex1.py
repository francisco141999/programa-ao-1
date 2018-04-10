"""def user/passw ():"""
user = "aluno"
passw = "Estg18"

def validarlogin () :
    conta = 0
    while conta != 3:
        utilizador =input("Introduza o utilizador: ")
        password =input("Introduza a password: ")
        if user == utilizador and passw == password:
            print("Login com sucesso")
        else:
            print("Login sem sucesso")

"""conta += 1"""

validarlogin()            




