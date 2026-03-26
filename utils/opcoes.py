'''Essa função é chamada quando o usuário digita uma opção válida no menu.
Ela é responsável por chamar a função correspondente à opção escolhida pelo usuário.
E também é responsável por tratar as exceções caso o usuário digite uma opção inválida.'''

from services.cadastrar_restaurantes import cadastrar_restaurantes
from services.listar_restaurantes import listar_restaurantes
from services.ativar_restaurantes import ativar_restaurantes
from utils.opcao_invalida import opcao_invalida


def escolher_opcao(opcao, restaurantes):    
        if opcao == 1:
            cadastrar_restaurantes(restaurantes)

        elif opcao == 2:
            listar_restaurantes(restaurantes)

        elif opcao == 3:
            ativar_restaurantes(restaurantes)

        elif opcao == 4:
            return

        else:
            opcao_invalida()