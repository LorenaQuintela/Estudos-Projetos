'''Crie uma lista com números repetidos, e através da  conversão desta para um conjunto, elimine os valores duplicados.'''

lista_numeros = [1, 4, 3, 1, 6, 5, 3]
print(f"tipo da lista: {type(lista_numeros)}")
print(lista_numeros)

#Transformando a lista em conjunto, usando o set que cria conjuntos únicos eliminando as duplicatas.

conjunto_convertido = set(lista_numeros)
print(f"Tipo do conjunto convertido: {type(conjunto_convertido)}")
print(conjunto_convertido)

#Tranformando o conjunto em lista novamente após ser atualizado com a eliminação das duplicadas
lista_convertida = list(conjunto_convertido)
print(f"Tipo da lista convertida: {type(lista_convertida)}")