'''Essa função é responsável por limpar o terminar,
garantindo uma melhor experiência para o usuário, 
evitando que a tela fique poluída com informações antigas.'''

def limpar_terminal():
    import os
    os.system("cls" if os.name == "nt" else "clear")