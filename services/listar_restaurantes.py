'''Essa função é chamada quando o usuário digita a opção 2 do menu.
Ela é responsável por listar todos os restaurantes cadastrados.'''

from utils.limpar_terminal import limpar_terminal
from utils.subtitulo import subtitulo


def listar_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Lista de Restaurantes Cadastrados")

    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    print("-" * 60)

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "Ativo" if restaurante["ativo"] else "Inativo"
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")

    input("\n Pressione Enter para continuar...")