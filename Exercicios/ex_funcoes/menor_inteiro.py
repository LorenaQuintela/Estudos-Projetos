'''Dado um vetor de números inteiros sua solução deve encontrar o menor número de inteiros. Exemplo: 
- Dada [31, 15, 88, 2] a sua solução, retornará 2
- Dada [34,  -345, -1, 100] a sua solução, retornará -345.'''

def encontrar_menor_inteiro(lista):
  menor = lista[0] # Vai receber o primeiro elemento da minha lista.

  for num in lista:
    if num < menor:
      menor = num # Se menor valor ele atualiza esse valor e vai para o proximo número.

  return menor

array_numeros = [34, 15, 88, 2]
resultado_menor = encontrar_menor_inteiro(array_numeros)
print(f"O menor valor do primeiro caso é: {resultado_menor}")

array_numeros = [34,-345, -1, 100]
resultado_menor = encontrar_menor_inteiro(array_numeros)
print(f"O menor valor do segundo caso é: {resultado_menor}")