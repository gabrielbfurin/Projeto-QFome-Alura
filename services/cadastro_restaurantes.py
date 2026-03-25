'''Essa função é chamada quando o usuário digita a opção 1 do menu.
Ela é responsável por cadastrar um novo restaurante, solicitando ao
usuário algumas informações necessárias para o cadastro.'''

from utils.limpar_terminal import limpar_terminal
from utils.subtitulo import subtitulo

def cadastro_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Cadastro de Restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    restaurantes.append(nome_do_restaurante)
    
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso! \n")
    input("\nPressione Enter para continuar...")

