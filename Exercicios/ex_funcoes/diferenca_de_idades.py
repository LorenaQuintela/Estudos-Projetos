'''No encontro familiar anual, a familia gosta de descobrir a idade do membro mais velho e do mais novo da familia e calcular a diferença entre elas.

Você receberá uma lista com as idades de todos, em qualquer ordem. As idades serão dadas em números inteiros, "então um bebê de 5 meses terá a idade atribuida a 0". Retorne um novo array(uma tupla)com: 

(idade do membro mais novo, idade do membro mais velho, diferença entre a idade do membro mais novo e a do membro mais velho).'''

def encontrar_diferença_de_idade(lista):
  mais_novo = lista[0]
  mais_velho = lista[0]
  

  for idade in lista:
    if idade < mais_novo:
      mais_novo = idade
    
    elif idade > mais_velho:
      mais_velho = idade

  difenca = mais_velho - mais_novo
  tupla_resultado = (mais_novo, mais_velho, difenca)

  return tupla_resultado

lista_idades = [57, 81, 14, 7, 32, 99]
resultado = encontrar_diferença_de_idade(lista_idades)

print("Mais novo, mais velho, e a diferença entre elas.")
print(resultado)