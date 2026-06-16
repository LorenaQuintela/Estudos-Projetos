'''Dado um conjunto de números, retorne o inverso aditivo de cada um. Cada número positivo se torna negativo e os negativos se tornam positivos.'''

def inverter_valores(lista_numeros):
    lista_invertida = []

    for valor in lista_numeros: #Pegar cada item.
        valor_invertido = valor * -1 # Com esse valor, multiplicar por -1 (sinal trocado)
        lista_invertida.append(valor_invertido) #  E guardo o valor invertido dentro da lista investida

    return lista_invertida

#Lista positiva se tornando negativa
lista_valores = [1, 2, 3, 4, 5]
print(inverter_valores(lista_valores))

#Lista mista tornando valor positivo em negativo e negativo em positivo.
lista_valores = [1, -2, 3, -4, 5]
print(inverter_valores(lista_valores))

#Lista vazia tem que retornar lista vazia
lista_valores = []
print(inverter_valores(lista_valores))