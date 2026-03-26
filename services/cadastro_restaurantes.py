'''Essa função é chamada quando o usuário digita a opção 1 do menu.
Ela é responsável por cadastrar um novo restaurante, solicitando ao
usuário algumas informações necessárias para o cadastro.'''

from utils.limpar_terminal import limpar_terminal
from utils.subtitulo import subtitulo

def cadastro_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Cadastro de Restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria_do_restaurante = input(f"Digite a categoria do {nome_do_restaurante}: ")
    
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo": False} # Cria um dicionário com as informações do restaurante a ser cadastrado.
    restaurantes.append(dados_do_restaurante) # Adiciona o dicionário criado à lista de restaurantes cadastrados.
    
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso! \n")
    input("\nPressione Enter para continuar...")

