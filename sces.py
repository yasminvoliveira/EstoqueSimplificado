## Sistema de Estoque
#print("Vamos começar a organizar nosso estoque!")


Produtos = [[0,"Pipoca",2,1],
            [1,"Amendoim", 5,2],
        [2,"Paçoca", 10,3]]

novoid = 2
quantidade = 0


## Definindo produtos para matriz

#Cadastrando Produtos
def novoprodutos():
    global Produtos
    global novoid
    global quantidade

    novoid = novoid + 1

    novoproduto = input("Insira o nome do produto que deseja adicionar:")

    quantidade = int(input("Insira a quantidade do produto que deseja adicionar:"))
    if quantidade <0:
        print("Insuficiente, tente novamente...")
        travarMenu()
    return
    localizacao = input("Insira a localização do produto que deseja adicionar:")

    Produtos.append([novoid, novoproduto, quantidade, localizacao])
    travarMenu()


## função para listar o estoque
def estoque():
    global Produtos
    print("-------- ESTOQUE -------")
    print(Produtos)
    print ("------------------------")
    travarMenu()


## Buscando produtos por ID
def buscando_id():
    global novoid

    produtoid_procurado = int(input("Digite o ID do produto que deseja procurar:"))

    if len(Produtos) == 0:
        print("Não há produtos no estoque para buscar, adicione um produto!")
        print("Para adicionar um produto selecione 1")

    
    else:
        colunaProcurada = -1
        for i in range (len(Produtos)):
            if(Produtos[i][0] == produtoid_procurado):
                colunaProcurada = i
                print(f"O ID {produtoid_procurado} está na linha {colunaProcurada}")
                print(colunaProcurada)
    travarMenu()

## Atualizando a quantidade de produtos no estoque
def Qtd_Produto():

    coluna = -1
    ProdutoP = int(input("Digite o ID do produto que deseja alterar a quantidade:"))
    
    for i in range (len(Produtos)):
        if(Produtos[i][0] == ProdutoP):
            coluna = i 
            novaqnt = int(input(("Digite a nova quantidade:")))
            
            if novaqnt<= 0:
                Produtos.pop(ProdutoP)
                print("O Produto foi excluído do estoque")


            else:
                Produtos[i][2] = (novaqnt)
                print("O estoque atualizado ficou:")
                print(Produtos)
                travarMenu()

    if coluna == -1:
        print("O produto não está cadastrado!")
        novoprodutos()

def travarMenu():
    input("\nPressione <ENTER> para continuar....")

## Menu
while True: ##Repete
    print("| 1 - Adicionar produto \n| 2 - Listar Todos os Produtos \n| 3 - Buscar Produto por ID \n| 4 - Atualizar Quantidades no Estoque \n| 5 - Sair do Programa \n")
    opcao = input("Digite a opção que deseja:")

    if opcao == "1":
        novoprodutos()
    elif opcao == "2":
        estoque()
    elif opcao == "3":
        buscando_id()
    elif opcao == "4":
        Qtd_Produto()
    elif (opcao == "5"):
        print("")
        break


    ## Discuti com Zanata