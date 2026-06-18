## Estoque Simplificado

print("Vamos começar a organizar nosso estoque!")
Produtos = [
    []
]

## Definindo produtos para matriz

def novoprodutos ():
    global Produtos
    novoid = input("Insira o ID novo:")
    novoproduto = input("Insira o nome do produto que deseja adicionar:")
    quantidade = input("Insira a quantidade do produto que deseja adicionar:")
    localização = input("Insira a localização do produto que deseja adicionar:")

## função para organizar
def estoque():
    print("-------- ESTOQUE -------")

## Buscando produtos por ID
def buscando_id():
    produto_procurado = input("Digite o ID do produto que deseja procurar:")
    colunaProcurada = -1
    for i in range (len(Produtos)):
        if(Produtos[i] == produto_procurado):
            colunaProcurada = i
## Menu
while True: ##Repete
    global opcao
    print("1 - Adicionar produto | 2 - Listar Todos os Produtos | 3 - Buscar Produto por ID | 4 - Atualizar Estoque | 5 - Sair do Programa ")
    opcao = input("Digite a opção que deseja:")

if opcao == 1:
    pass