def login(utilizador,password):
    user = "aluno"
    passw = "Estg18"
    if user == utilizador and passw == password:
        return True
    return False

def validarlogin () :
        conta = 0
        while conta < 3:

            utilizador =input("Introduza o utilizador: ")  # ggggg
            password =input("Introduza a password: ") # 123
            if login(utilizador,password): 
                print("Login com sucesso")
                break
            else:
                print("Login sem sucesso")
            conta += 1

validarlogin()            




