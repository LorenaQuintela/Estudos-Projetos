'''Crie uma lista chamada países com alguns nomes dentro dela. Em seguida: 
- Adicione um novo país ao fim da lista
- Adicione um novo país logo antes da posição 1.
- Remova um país pelo nome
- Remova um país pelo índice 
- Mostre o total de países.'''

lista_paises = ["Escócia", "Inglaterra", "Brasil", "Chile", "Grécia"]
lista_paises.append("Colômbia")
print(lista_paises)
lista_paises.insert(0, "Estados Unidos")
print(lista_paises)
lista_paises.remove("Chile")
print(lista_paises)
lista_paises.pop(0)
print(lista_paises)
print(f"A quantidade de países depois de todos os parâmetros é: {len(lista_paises)}" )