from random import randint
import time
import re
class utilizador():
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.password = ""
        self.identificador = ""
        self.resposta = ""
        self.data = ""
        self.bloquear = ""
    
    def login_utilizador(self):
        contar = 0
        if self.bloquear == True:
            pergunta_resposta = input("Responder a pergunta de segurança: ")
            while pergunta_resposta != self.respost:
                pergunta_resposta = input("Responder a pergunta de segurança: ")
            else:
                self.bloquear = False   
                utilizador1.login_utilizador()
        while contar < 3:
            login_email = input("Email: ")
            login_password = input("Password: ")
            if self.email == login_email and self.password == login_password:
                print("Entrou na sua conta")
                break
            else:
                print("Errado de acesso ao login! ")
                contar += 1
        else:
            print("Utilizador foi bloqueado ")
            self.bloquear = True
            utilizador1.login_utilizador()
                      
print("Introduzir dados para o utilizador1: ")
utilizador1 = utilizador()
utilizador1.nome = input("Nome de utilizador: ")
utilizador1.email = input("Email do utilizador: ")
utilizador1.password = input("Palavra-passe do utilizador: ")
utilizador1.identificador = "{}--{}".format(randint(100, 999),randint(1000, 9999))
utilizador1.resposta = input("Resposta secreta do utilizador: ")
utilizador1.data = time.strftime("%d/%m/%Y")

print("Introduzir dados para o utilizador2")
utilizador2 = utilizador()
utilizador2.nome = input("Nome de utilizador: ")
utilizador2.email = input("Email do utilizador: ")
utilizador2.password = input("Palavra-passe do utilizador: ")
utilizador2.identificador = "{}--{}".format(randint(100, 999),randint(1000, 9999))
utilizador2.respost = input("Resposta secreta do utilizador: ")
utilizador2.data = time.strftime("%d/%m/%Y")

utilizador1.login_utilizador()