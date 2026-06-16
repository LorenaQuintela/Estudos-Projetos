'''
Escreva uma função, que receba uma lista com vários itens, mais que contenha um único elemento com nome "agulha".
Após achar a agulha, retorne uma mensagem que diga: Agulha encontrada na posição x .'''

def encontrar_agulha_no_palheiro(palheiro):
  posicao = 0 
    
  for item in palheiro:
    if item == "agulha":
      break
      
    posicao = posicao +1

  return f"Encontrei a agulha na posição: {posicao}"

#Exemplo na posição 5
varios_itens = ["alfinete", "botão", "linha", "fita", "argola", "agulha", "marcador" ]
print(encontrar_agulha_no_palheiro
(varios_itens))

#Exemplo na posição 0
varios_itens = ["agulha", "botão", "linha", "fita", "argola", "alfinete" , "marcador" ]
print(encontrar_agulha_no_palheiro(varios_itens))

#Exemplo na posição 6
varios_itens = ["alfinete", "botão", "linha", "fita", "argola", "marcador", "agulha" ]
print(encontrar_agulha_no_palheiro(varios_itens))