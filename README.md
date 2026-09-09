# QFome — Sistema de Gerenciamento de Restaurantes

Aplicação de terminal desenvolvida em **Python** para cadastro e gerenciamento de restaurantes.

O projeto foi criado durante o curso **Python: crie a sua primeira aplicação**, da Alura, e posteriormente organizado em múltiplos módulos para praticar lógica de programação, separação de responsabilidades e estruturação de projetos Python.

## Funcionalidades

- Cadastro de restaurantes
- Listagem dos restaurantes cadastrados
- Ativação e desativação de restaurantes
- Validação de opções inseridas pelo usuário
- Verificação de restaurantes duplicados
- Interface organizada pelo terminal

## Estrutura do projeto

```text
Projeto-QFome-Alura/
├── app/
│   ├── __init__.py
│   └── main.py
│
├── services/
│   ├── __init__.py
│   ├── ativar_restaurantes.py
│   ├── cadastrar_restaurantes.py
│   └── listar_restaurantes.py
│
├── ui/
│   ├── __init__.py
│   └── menu.py
│
├── utils/
│   ├── __init__.py
│   ├── limpar_terminal.py
│   ├── opcao_invalida.py
│   ├── opcoes.py
│   └── subtitulo.py
│
└── README.md
```

A aplicação foi dividida em módulos responsáveis pela interface, regras relacionadas aos restaurantes, funções auxiliares e inicialização do sistema.

## Demonstração

### Menu principal

<img width="797" height="457" alt="image" src="https://github.com/user-attachments/assets/e1376f28-2381-4c0c-a1bf-127352ea9fb2" />

O sistema apresenta um menu interativo pelo terminal com as opções disponíveis para o usuário.

### Fluxo da aplicação

<img width="573" height="207" alt="image" src="https://github.com/user-attachments/assets/247458f9-e5ec-4f09-b9d1-e7ca1de5cb19" />

<img width="673" height="133" alt="image" src="https://github.com/user-attachments/assets/1b675bac-5441-469b-b55d-1ce792589298" />

É possível cadastrar restaurantes, visualizar os registros existentes e alterar o status de cada restaurante entre ativo e inativo.

**[Assista ao sistema em execução](https://1drv.ms/v/c/e02e5abde513647c/IQB936BfrNrrR5srX__UYfWkASibDpnr9si4LeG3z8rFsR8?e=pdEjMJ)**

## Tecnologias utilizadas

- Python
- Git
- GitHub
- VS Code

O projeto utiliza apenas recursos da biblioteca padrão do Python e não possui dependências externas.

## Como executar

### 1. Pré-requisitos

Tenha o **Python 3.10 ou superior** instalado.

Para verificar:

```bash
python --version
```

### 2. Clone o repositório

```bash
git clone https://github.com/gabrielbfurin/Projeto-QFome-Alura.git
```

### 3. Entre na pasta

```bash
cd Projeto-QFome-Alura
```

### 4. Execute a aplicação

```bash
python -m app.main
```

No Windows, também é possível utilizar:

```bash
py -m app.main
```

Se estiver utilizando o VS Code, o projeto também possui uma configuração de **Run and Debug** para executar a aplicação diretamente pelo editor.

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei principalmente:

- organização de um projeto em múltiplos arquivos;
- modularização com pacotes Python;
- criação e reutilização de funções;
- manipulação de listas e dicionários;
- tratamento de erros com `try/except`;
- validação de entradas;
- separação de responsabilidades entre diferentes módulos;
- uso de Git e GitHub para versionamento.

## Possíveis evoluções

Algumas funcionalidades que poderiam ser adicionadas em versões futuras:

- persistência dos restaurantes em arquivo;
- busca por restaurante;
- edição e exclusão de registros;
- testes automatizados;
- exposição das funcionalidades através de uma API.

## Autor

Desenvolvido por **Gabriel Furin**.
