'''Essa função é chamada quando o usuário digita uma opção válida no menu.
Ela é responsável por chamar a função correspondente à opção escolhida pelo usuário.
E também é responsável por tratar as exceções caso o usuário digite uma opção inválida.'''

import os
import time


from funcoes import cadastro, listar, ativacao, opcao_invalida

def escolher_opcao(opcao, restaurantes):    
        if opcao == 1:
            cadastro.cadastro(restaurantes)
        elif opcao == 2:
            listar.listar_restaurantes(restaurantes)
        elif opcao == 3:
            ativacao.ativar_restaurante(restaurantes)
        elif opcao == 4:
            print("Saindo...")
            time.sleep(2)
            os.system("cls")
        else:
            opcao_invalida.opcao_invalida()