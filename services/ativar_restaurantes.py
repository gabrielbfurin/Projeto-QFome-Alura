from utils.subtitulo import subtitulo
from utils.limpar_terminal import limpar_terminal

def ativar_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Ativação de Restaurantes")

    nome_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")
    procurar_restaurante = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            procurar_restaurante = True
            restaurante["ativo"] = not restaurante["ativo"] # Inverte o valor do campo "ativo" do restaurante encontrado (se for True, passa a ser False, e vice-versa).

            mensagem_status = f"O restaurante '{nome_restaurante}' foi ativado!" if restaurante["ativo"] else f"O restaurante '{nome_restaurante}' foi desativado!"
            print(mensagem_status)

    if not procurar_restaurante:
        print(f"Restaurante '{nome_restaurante}' não encontrado.")

    input("\nPressione Enter para continuar...")