# Sistema de Estoque

-> Este é um programa simples em Python que fiz com matrizes e funções. Ele roda direto no terminal e serve para gerenciar uma lista/estoque de produtos.

## O que o programa faz:
* **Adiciona produtos**: Cadastra um item novo com id, nome, quantidade e localização.
* **Mostra o estoque**: Lista tudo o que está guardado no sistema (produtos e suas informações).
* **Busca por ID**: Procura um produto usando o número de identificação dele.
* **Atualiza quantidades**: Muda o estoque de um produto. Se a quantidade chegar a zero, o item é apagado;

## O que o programa determina:
        * Apresenta um Menu Interativo;
        * O ID é dado automaticamente pelo sistema;
        * Quando é adicionado quantidades negativas, ele retorna ao menu.

# O que o usuário pode fazer no sistema:
**Adicionar produtos** : Determinar o nome, a quantidade e a localização;
**Buscar por ID** : Procurar um determinado produto pelo seu ID;
**Atualizar quantidades** : Alterar a quantidade de cada produto do estoque.

## O que usei:
* Estrutura de repetição `while` para o menu principal;
* Condicionais `if/elif/else` para escolher as opções;
* Listas dentro de listas (matrizes) para armazenar os dados dos produtos no estoque;
* Funções (`def`) para organizar cada função do sistema.