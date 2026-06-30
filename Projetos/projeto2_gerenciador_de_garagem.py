# Crud de carros -> Gerenciador de Garagem que permita cadastrar, listar, editar, deletar e sair.
def Cadastrar_carro(placa, cor, modelo, ano):
  placa = input("Digite a placa: ")
  cor = input("Digite a cor: ")
  modelo = input("Digite o modelo: ")
  ano = input("Digite o ano: ")

  return placa, cor, modelo, ano

def Listar_carro(lista):
  return lista

def Editar_carro():
  return

def Deletar_carro(placa):
  placa = input("Digite a placa: ")



print("--- GERENCIADOR DE GARAGEM ---\n")
print("1 - Cadastrar um carro")
print("2 - Listar carros")
print("3 - Editar carro")
print("4 - Deletar carro")
print("5 - Sair")

opção = input("Escolha uma opção: ")

if opção == "1":
  cadastrar_carro()