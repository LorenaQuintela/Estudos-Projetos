def quebrando_lista(lista_entrada):
  lista_resultante = []
  tam_lista = len(lista_entrada)
  espaco = " "

  #range (1, 5) -> (1, 2, 3, 4)
  for limite in range(1, tam_lista):
    primeiro_pedaco_sublista = lista_entrada[:limite] 
    segundo_pedaco_sublista = lista_entrada[limite:]
  
    #Usar join tendo como separador os espaços para conter uma string só separada por espaços.
    primeiro_pedaco_str = espaco.join(primeiro_pedaco_sublista)
    segundo_pedaco_str = espaco.join(segundo_pedaco_sublista)

    #Criando a tupla para converter os pedaçõs na forma de strings. Adicionar ela com append na lista resultando para ser retornada.
    tupla = (primeiro_pedaco_str, segundo_pedaco_str)
    lista_resultante.append(tupla)
    
  return lista_resultante

lista_palavras = ["az", "toto", "picaro", "zone", "kiwi"]
res = quebrando_lista(lista_palavras)
print(res)