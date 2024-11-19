# Variável que armazena um nome
nome = 'John'

# Lista que armazena as compras
lista_de_compras = ['Café', 'Açúcar', 'Coador', 'Cafeteira']

# Função para exibir a lista de compras
def exibir_lista():
    print(f"\nA lista de compras do {nome} é:")
    if lista_de_compras:
        for i, item in enumerate(lista_de_compras, start=1):
            print(f" {i}. {item}")
    else:
        print(" A lista está vazia.")

# Loop para adicionar/remover itens da lista
while True:
    exibir_lista()
    
    # Menu de opções
    print("\nOpções:")
    print(" 1. Adicionar item")
    print(" 2. Remover item")
    print(" 3. Sair")
    
    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == '1':
        novo_item = input("Digite o item que deseja adicionar: ")
        lista_de_compras.append(novo_item)
        print(f"'{novo_item}' foi adicionado à lista.")
    elif escolha == '2':
        item_remover = input("Digite o número ou o nome do item para remover: ")
        if item_remover.isdigit():  # Remover pelo número
            indice = int(item_remover) - 1
            if 0 <= indice < len(lista_de_compras):
                removido = lista_de_compras.pop(indice)
                print(f"'{removido}' foi removido da lista.")
            else:
                print("Número inválido.")
        else:  # Remover pelo nome
            if item_remover in lista_de_compras:
                lista_de_compras.remove(item_remover)
                print(f"'{item_remover}' foi removido da lista.")
            else:
                print(f"'{item_remover}' não está na lista.")
    elif escolha == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
