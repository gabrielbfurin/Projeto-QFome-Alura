'''Essa função é chamada quando o usuário digita a opção 2 do menu.
Ela é responsável por listar todos os restaurantes cadastrados.'''

from utils.limpar_terminal import limpar_terminal
from utils.subtitulo import subtitulo


def listagem_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Lista de Restaurantes Cadastrados")

    for restaurante in restaurantes:
        print(f"- {restaurante}")

    input("\n Pressione Enter para continuar...")