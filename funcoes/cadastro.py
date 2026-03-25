'''Essa função é chamada quando o usuário digita a opção 1 do menu.
Ela é responsável por cadastrar um novo restaurante, solicitando ao
usuário algumas informações necessárias para o cadastro.'''

import os

def cadastro(restaurantes):
    os.system("cls" if os.name == "nt" else "clear")

    print("=== Cadastro de Restaurante === \n")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    restaurantes.append(nome_do_restaurante)
    
    print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso! \n")
    input("Pressione Enter para continuar...")

