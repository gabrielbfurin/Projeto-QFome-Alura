'''Essa função é chamada quando o usuário digita a opção 1 do menu.
Ela é responsável por cadastrar um novo restaurante, solicitando ao
usuário algumas informações necessárias para o cadastro.'''

from utils.limpar_terminal import limpar_terminal
from utils.subtitulo import subtitulo

def cadastrar_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Cadastro de Restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante: ")

    for r in restaurantes:
        if nome_do_restaurante.strip().lower() == r["nome"].strip().lower(): # Verifica se o nome do restaurante digitado pelo usuário já existe na lista de restaurantes cadastrados, ignorando espaços em branco e diferenças de maiúsculas/minúsculas.
            print(f"Restaurante '{nome_do_restaurante}' já cadastrado!")
            input("\nPressione Enter para continuar...")
            return

    categoria_do_restaurante = input(f"Digite a categoria do {nome_do_restaurante}: ")
    
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo": False} # Cria um dicionário com as informações do restaurante a ser cadastrado.
    restaurantes.append(dados_do_restaurante) # Adiciona o dicionário criado à lista de restaurantes cadastrados.
    
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso! \n")
    input("\nPressione Enter para continuar...")

