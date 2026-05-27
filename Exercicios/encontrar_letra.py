'''
Faça um programa que receba uma string e responda se ela tem uma vogal, se sim. Quais são? E também diga se ela é uma frase ou não.'''

frase = 'Lorena está tentando resolver!'
vogal_procurada = 'e'

if vogal_procurada in frase:
  print(f"Sim, A vogal '{vogal_procurada}' existe na frase.")
else:
  print(f"A vogal '{vogal_procurada}' não existe na frase.")

if " " in frase:
  print("É uma frase!")
else:
  print("Não é uma frase!")