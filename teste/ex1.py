class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""

class tabuleiro():

    def __init__(self,):
        self.tabuleiro = [[None, None ,None ], 
                          [None, None ,None ], 
                          [None, None ,None ]]

    def printTabuleiro(self):
        print(' | A | B | C |')
        print( '--------------')
        print( '1| '   '  | '   '  | '   '  |')
        print( '--------------')
        print( '2| '   '  | '   '  | '   '  |') 
        print( '--------------')
        print( '3| '   '  | '   '  | '   '  |')
        print( '--------------')

tabuleiro1 = tabuleiro()
tabuleiro1.tabuleiro = [ [None, None ,None ], 
                         [None, None ,None ], 
                         [None, None ,None ] ]
    
jogador1 = jogador()
jogador1.nome = input("Nome do jogador: ")
jogador1.token = input("Token que o jogador1 pretende usar: ")

jogador2 = jogador()
jogador2.nome = input("Nome do jogador: ")
jogador2.token = input("Token que o jogador2 pretende usar: ")

while True:
    if jogador1.token == jogador2.token: 
        jogador2.token = input("Token que o jogador 2 que prente usar: ")
    else:
        break

tabuleiro1.printTabuleiro()
print(jogador1.nome,jogador1.token,jogador2.nome,jogador2.token)

jogar = tabuleiro()
numero_max_jogadas = 9
while numero_max_jogadas <= 9:
    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
    