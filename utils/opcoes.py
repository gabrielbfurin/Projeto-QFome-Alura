'''Essa função é chamada quando o usuário digita uma opção válida no menu.
Ela é responsável por chamar a função correspondente à opção escolhida pelo usuário.
E também é responsável por tratar as exceções caso o usuário digite uma opção inválida.'''

from services.cadastro_restaurantes import cadastro_restaurantes
from services.listagem_restaurantes import listagem_restaurantes
from services.ativacao_restaurantes import ativacao_restaurantes
from utils.opcao_invalida import opcao_invalida
from utils.limpar_terminal import limpar_terminal
import time


def escolher_opcao(opcao, restaurantes):    
        if opcao == 1:
            cadastro_restaurantes(restaurantes)

        elif opcao == 2:
            listagem_restaurantes(restaurantes)

        elif opcao == 3:
            ativacao_restaurantes(restaurantes)

        elif opcao == 4:
            return

        else:
            opcao_invalida()