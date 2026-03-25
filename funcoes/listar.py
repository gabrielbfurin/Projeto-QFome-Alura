'''Essa função é chamada quando o usuário digita a opção 2 do menu.
Ela é responsável por listar todos os restaurantes cadastrados.'''

import os

def listar_restaurantes(restaurantes):
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Lista de Restaurantes Cadastrados === \n")

    for restaurante in restaurantes:
        print(f"- {restaurante}")

    input("\n Pressione Enter para continuar...")