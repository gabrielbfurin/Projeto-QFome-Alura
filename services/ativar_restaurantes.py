'''Essa função é responsável por ativar ou desativar o restaurante desejado pelo usuário.
Ela recebe a lista de restaurantes cadastrados, solicita ao usuário o nome do restaurante para que
seja ativado ou desativado, e então percorre a lista de restaurantes para encontrar o restaurante correspondente.'''

from utils.subtitulo import subtitulo
from utils.limpar_terminal import limpar_terminal

def ativar_restaurantes(restaurantes):
    limpar_terminal()
    subtitulo("Ativação de Restaurantes")

    nome_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")
    procurar_restaurante = False

    for restaurante in restaurantes:
        if nome_restaurante.strip().lower() == restaurante["nome"].strip().lower(): # Compara o nome do restaurante digitado pelo usuário com o nome do restaurante na lista, ignorando espaços em branco e diferenças de maiúsculas/minúsculas.
            procurar_restaurante = True
            restaurante["ativo"] = not restaurante["ativo"] # Inverte o valor do campo "ativo" do restaurante encontrado (se for True, passa a ser False, e vice-versa).

            mensagem_status = f"O restaurante '{nome_restaurante}' foi ativado!" if restaurante["ativo"] else f"O restaurante '{nome_restaurante}' foi desativado!"
            print(mensagem_status)

    if not procurar_restaurante:
        print(f"Restaurante '{nome_restaurante}' não encontrado.")

    input("\nPressione Enter para continuar...")