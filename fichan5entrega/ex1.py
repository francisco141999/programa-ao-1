"""from random import randint
import time
import re

def isValidEmail(utilizador_email):
    if len(email) > 7:
    if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
    return True
    return False
    if isValidEmail("my.email@gmail.com") == True :
    print "This is a valid email address"
    else:
    print "This is not a valid email address"

class owner():
    def __init__(self,utilizador_nome, utilizador_email,utlizador_identificador,utilizador_pass,utlizador_data_criacao,utilizador_resposta,=None):
        self.nome = utilizador_nome
        self.email = utilizador_email
        self.identificador = utilizador_identificador
        self.password = utilizador_password
        self.data = utlizador_data_criacao
        self.resposta = utilizador_resposta
                  
    def __str__(self):
        return "Nome: {} \nEmail: {} \nIdentificador: {} \nPassword: {} \nData de criaçao: {} \nResposta: {}".format(self.utilizador_nome, self.utilizador_email, self.utlizador_identificador, self.utilizador_password, self.utlizador_data_criacao, self.utilizador_resposta)

if __name__ == "__main__":
    
    p1 = Point(2, 3, "red")
    p2 = Point(10, 20)

    print(p1)
    print(p2)

    utilizador_nome = input ("Introduza o nome do utilizador: ")
    utilizador_email = input ("Introduza o email: ")
    utlizador_identificador = "{}-{}".format(randint(100,999),randint(1000,9999))
    utilizador_password = input ("Introduza a password: ")
    utlizador_data_criacao = time.strftime("%d:%m:%Y")
    utilizador_resposta = input("Introduza a resposta: ")  """



