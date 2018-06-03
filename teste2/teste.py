def menu():
    escolha = int(input('''
    Menu
1 - Iniciar o jogo 
2 - Ver Ranking
3 - Sair do jogo

Escolha: '''))
    if escolha == 1:
        print('Iniciar o jogo escolhida')
    elif escolha == 2:
        print('Ver Ranking escolhida')
    elif escolha == 3:
        print('Sair do jogo escolhida')
    else:
        print('Escolha invalida, tente novamente')
        menu()