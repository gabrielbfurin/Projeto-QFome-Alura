'''Essa função é o ponto de partida do programa. Ela é responsável por exibir o menu principal,
receber a opção escolhida pelo usuário e chamar a função correspondente para executar a ação desejada.'''

import time

from ui.menu import menu
from utils.opcao_invalida import opcao_invalida
from utils.limpar_terminal import limpar_terminal
from utils.opcoes import escolher_opcao

def main():
    restaurantes = [] # Lista para armazenar os restaurantes cadastrados - Vai ser usada na função cadastro()
    # para adicionar novos restaurantes e na função listar() para exibir os restaurantes cadastrados.

    while True:        
        limpar_terminal()

        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            opcao_invalida()
            continue

        escolher_opcao(opcao, restaurantes)

        if opcao == 4:
            print("Saindo...")
            time.sleep(2)
            limpar_terminal()
            break

if __name__ == "__main__":    
    main()