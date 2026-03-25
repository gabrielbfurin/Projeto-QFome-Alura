import os
import time

from funcoes import menu, escolher_opcao, cadastro, listar, ativacao, opcao_invalida


def main():
    restaurantes = [] # Lista para armazenar os restaurantes cadastrados - Vai ser usada na função cadastro()
    # para adicionar novos restaurantes e na função listar() para exibir os restaurantes cadastrados.

    while True:        
        os.system("cls" if os.name == "nt" else "clear")

        menu.menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            opcao_invalida.opcao_invalida()
            continue

        escolher_opcao.escolher_opcao(opcao, restaurantes)

        if opcao == 4:
            print("Saindo...")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            break

if __name__ == "__main__":    
    main()