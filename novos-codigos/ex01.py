# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

nome = 'John'
lista_de_compras = ['Café', 'Açucar', 'Coador', 'Cafeteira']

print(f"A lista de compras do {nome} é:")
for i, item in enumerate(lista_de_compras, start=1):
    print(f" {i}.{item}")